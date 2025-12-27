"""Demo connector for testing and examples."""

import random
from datetime import datetime, timedelta
from typing import Any

from bizmetrics.connectors.base import BaseConnector


class DemoConnector(BaseConnector):
    """Demo connector that generates sample business metrics."""

    name = "demo"
    description = "Demo connector with sample business metrics data"

    def fetch(
        self,
        start_date: str | None = None,
        end_date: str | None = None,
        **kwargs: Any,
    ) -> list[dict[str, Any]]:
        """Generate sample metrics data.

        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format

        Returns:
            List of sample metric records
        """
        # Parse dates or use defaults
        if start_date:
            start = datetime.strptime(start_date, "%Y-%m-%d")
        else:
            start = datetime.now() - timedelta(days=30)

        end = datetime.strptime(end_date, "%Y-%m-%d") if end_date else datetime.now()

        # Generate sample data
        data: list[dict[str, Any]] = []
        current = start

        while current <= end:
            data.append({
                "date": current.strftime("%Y-%m-%d"),
                "sessions": random.randint(1000, 5000),
                "page_views": random.randint(3000, 15000),
                "bounce_rate": round(random.uniform(30, 70), 2),
                "avg_session_duration": round(random.uniform(60, 300), 2),
                "conversions": random.randint(10, 100),
                "revenue": round(random.uniform(500, 5000), 2),
            })
            current += timedelta(days=1)

        return data

    def validate_credentials(self) -> bool:
        """Demo connector always returns True for credentials."""
        return True

    def get_available_metrics(self) -> list[str]:
        """Get available demo metrics."""
        return [
            "sessions",
            "page_views",
            "bounce_rate",
            "avg_session_duration",
            "conversions",
            "revenue",
        ]
