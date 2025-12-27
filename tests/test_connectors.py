"""Tests for data connectors."""

from datetime import datetime, timedelta

import pytest

from bizmetrics.connectors.demo import DemoConnector


class TestDemoConnector:
    """Test suite for DemoConnector."""

    def test_fetch_returns_list(self) -> None:
        """Test that fetch returns a list of records."""
        connector = DemoConnector()
        data = connector.fetch()
        
        assert isinstance(data, list)
        assert len(data) > 0

    def test_fetch_record_structure(self) -> None:
        """Test that each record has expected fields."""
        connector = DemoConnector()
        data = connector.fetch()
        
        expected_fields = {
            "date", "sessions", "page_views", "bounce_rate",
            "avg_session_duration", "conversions", "revenue"
        }
        
        for record in data:
            assert set(record.keys()) == expected_fields

    def test_fetch_with_date_range(self) -> None:
        """Test fetch with specific date range."""
        connector = DemoConnector()
        start = "2024-01-01"
        end = "2024-01-07"
        
        data = connector.fetch(start_date=start, end_date=end)
        
        assert len(data) == 7  # 7 days inclusive

    def test_validate_credentials(self) -> None:
        """Test that demo connector always validates."""
        connector = DemoConnector()
        assert connector.validate_credentials() is True

    def test_get_available_metrics(self) -> None:
        """Test available metrics list."""
        connector = DemoConnector()
        metrics = connector.get_available_metrics()
        
        assert "sessions" in metrics
        assert "revenue" in metrics
        assert len(metrics) == 6
