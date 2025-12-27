"""CSV exporter."""

import csv
from pathlib import Path
from typing import Any


class CSVExporter:
    """Export metrics to CSV format."""

    def export(self, data: list[dict[str, Any]], output_path: Path) -> None:
        """Export data to CSV file.

        Args:
            data: List of metric records
            output_path: Output file path
        """
        if not data:
            return

        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
