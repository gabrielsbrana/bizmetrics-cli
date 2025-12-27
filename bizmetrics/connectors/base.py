"""Base connector interface."""

from abc import ABC, abstractmethod
from typing import Any


class BaseConnector(ABC):
    """Abstract base class for data connectors."""

    name: str = "base"
    description: str = "Base connector interface"

    @abstractmethod
    def fetch(
        self,
        start_date: str | None = None,
        end_date: str | None = None,
        **kwargs: Any,
    ) -> list[dict[str, Any]]:
        """Fetch metrics data from the source.

        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            **kwargs: Additional connector-specific parameters

        Returns:
            List of metric records as dictionaries
        """
        pass

    @abstractmethod
    def validate_credentials(self) -> bool:
        """Validate connector credentials.

        Returns:
            True if credentials are valid, False otherwise
        """
        pass

    def get_available_metrics(self) -> list[str]:
        """Get list of available metrics from this connector.

        Returns:
            List of metric names
        """
        return []
