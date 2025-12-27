"""Excel exporter."""

from pathlib import Path
from typing import Any

import pandas as pd


class ExcelExporter:
    """Export metrics to Excel format."""

    def export(self, data: list[dict[str, Any]], output_path: Path) -> None:
        """Export data to Excel file.

        Args:
            data: List of metric records
            output_path: Output file path
        """
        if not data:
            return

        output_path.parent.mkdir(parents=True, exist_ok=True)

        df = pd.DataFrame(data)

        with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
            df.to_excel(writer, sheet_name="Metrics", index=False)

            # Auto-adjust column widths
            worksheet = writer.sheets["Metrics"]
            for idx, col in enumerate(df.columns):
                max_length = max(
                    df[col].astype(str).map(len).max(),
                    len(col)
                ) + 2
                worksheet.column_dimensions[chr(65 + idx)].width = max_length
