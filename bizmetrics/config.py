"""Configuration management using Pydantic Settings."""

from functools import lru_cache
from pathlib import Path
from typing import Any, Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings with environment variable support."""

    model_config = SettingsConfigDict(
        env_prefix="BIZMETRICS_",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # Directories
    cache_dir: Path = Field(
        default=Path.home() / ".bizmetrics" / "cache",
        description="Directory for cache storage",
    )
    log_dir: Path = Field(
        default=Path.home() / ".bizmetrics" / "logs",
        description="Directory for log files",
    )

    # Logging
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = Field(
        default="INFO",
        description="Logging level",
    )

    # Export defaults
    default_format: Literal["csv", "excel", "json"] = Field(
        default="csv",
        description="Default export format",
    )

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        # Ensure directories exist
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.log_dir.mkdir(parents=True, exist_ok=True)


@lru_cache
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings()
