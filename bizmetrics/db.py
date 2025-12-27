"""SQLite database for caching and configuration storage."""

import json
import sqlite3
from datetime import datetime
from pathlib import Path
from typing import Any, cast


class Database:
    """SQLite database handler for metrics caching."""

    def __init__(self, db_path: Path) -> None:
        """Initialize database connection."""
        self.db_path = db_path
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._init_schema()

    def _get_connection(self) -> sqlite3.Connection:
        """Get database connection."""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def _init_schema(self) -> None:
        """Initialize database schema."""
        with self._get_connection() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS metrics_cache (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    connector TEXT NOT NULL,
                    data TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    expires_at TEXT
                )
            """)
            conn.execute("""
                CREATE INDEX IF NOT EXISTS idx_connector
                ON metrics_cache(connector)
            """)
            conn.commit()

    def cache_metrics(
        self,
        connector: str,
        data: list[dict[str, Any]],
        ttl_hours: int = 24,
    ) -> None:
        """Cache metrics data."""
        now = datetime.now()
        expires = datetime.fromtimestamp(now.timestamp() + ttl_hours * 3600)

        with self._get_connection() as conn:
            # Clear old cache for this connector
            conn.execute(
                "DELETE FROM metrics_cache WHERE connector = ?",
                (connector,),
            )
            # Insert new data
            conn.execute(
                """
                INSERT INTO metrics_cache (connector, data, created_at, expires_at)
                VALUES (?, ?, ?, ?)
                """,
                (connector, json.dumps(data), now.isoformat(), expires.isoformat()),
            )
            conn.commit()

    def get_cached_metrics(self, connector: str) -> list[dict[str, Any]]:
        """Get cached metrics for a connector."""
        with self._get_connection() as conn:
            row = conn.execute(
                """
                SELECT data, expires_at FROM metrics_cache
                WHERE connector = ?
                ORDER BY created_at DESC
                LIMIT 1
                """,
                (connector,),
            ).fetchone()

            if not row:
                return []

            # Check expiration
            expires = datetime.fromisoformat(row["expires_at"])
            if datetime.now() > expires:
                return []

            return cast(list[dict[str, Any]], json.loads(row["data"]))

    def get_cache_stats(self) -> list[tuple[str, int, str]]:
        """Get cache statistics."""
        with self._get_connection() as conn:
            rows = conn.execute("""
                SELECT
                    connector,
                    json_array_length(data) as record_count,
                    created_at
                FROM metrics_cache
                ORDER BY created_at DESC
            """).fetchall()

            return [(row["connector"], row["record_count"], row["created_at"]) for row in rows]

    def clear_cache(self) -> None:
        """Clear all cached data."""
        with self._get_connection() as conn:
            conn.execute("DELETE FROM metrics_cache")
            conn.commit()
