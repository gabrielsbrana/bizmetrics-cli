"""CLI commands for BizMetrics using Typer."""

from pathlib import Path

import typer
from rich.console import Console
from rich.table import Table

from bizmetrics import __version__
from bizmetrics.config import get_settings
from bizmetrics.connectors.base import BaseConnector
from bizmetrics.connectors.demo import DemoConnector
from bizmetrics.db import Database
from bizmetrics.exporters.csv_exporter import CSVExporter
from bizmetrics.exporters.excel_exporter import ExcelExporter

app = typer.Typer(
    name="bizmetrics",
    help="🚀 Business Intelligence Metrics CLI - Fetch, analyze, and export your metrics",
    add_completion=False,
)
console = Console()


def version_callback(value: bool) -> None:
    """Show version and exit."""
    if value:
        console.print(f"[bold blue]BizMetrics CLI[/bold blue] version [green]{__version__}[/green]")
        raise typer.Exit()


@app.callback()
def main(
    version: bool | None = typer.Option(
        None,
        "--version",
        "-v",
        help="Show version and exit",
        callback=version_callback,
        is_eager=True,
    ),
) -> None:
    """BizMetrics CLI - Your business intelligence companion."""
    pass


@app.command()
def fetch(
    connector: str = typer.Argument(..., help="Connector name (demo, google-analytics, meta-ads)"),
    start_date: str | None = typer.Option(None, "--start-date", "-s", help="Start date (YYYY-MM-DD)"),
    end_date: str | None = typer.Option(None, "--end-date", "-e", help="End date (YYYY-MM-DD)"),
    cache: bool = typer.Option(True, "--cache/--no-cache", help="Use cache for results"),
) -> None:
    """Fetch metrics from a data connector."""
    from bizmetrics.connectors.google_analytics import GoogleAnalyticsConnector
    from bizmetrics.connectors.meta_ads import MetaAdsConnector

    settings = get_settings()
    db = Database(settings.cache_dir / "bizmetrics.db")

    console.print(f"[bold]Fetching metrics from [cyan]{connector}[/cyan]...[/bold]")

    # Select connector
    conn: BaseConnector
    if connector == "demo":
        conn = DemoConnector()
    elif connector == "google-analytics":
        conn = GoogleAnalyticsConnector()
        console.print("[dim]Using Google Analytics demo mode (no credentials configured)[/dim]")
    elif connector == "meta-ads":
        conn = MetaAdsConnector()
        console.print("[dim]Using Meta Ads demo mode (no credentials configured)[/dim]")
    else:
        console.print(f"[red]Unknown connector: {connector}[/red]")
        console.print("Available connectors: demo, google-analytics, meta-ads")
        raise typer.Exit(1)

    data = conn.fetch(start_date=start_date, end_date=end_date)

    if cache:
        db.cache_metrics(connector, data)
        console.print("[dim]Results cached.[/dim]")

    # Display results in a table
    table = Table(title=f"📊 Metrics from {connector}")
    if data:
        # Show first 5 columns max for readability
        columns = list(data[0].keys())[:7]
        for key in columns:
            table.add_column(key.replace("_", " ").title(), overflow="fold")

        # Show max 10 rows in terminal
        for row in data[:10]:
            table.add_row(*[str(row.get(c, ""))[:20] for c in columns])

        if len(data) > 10:
            table.add_row(*["..." for _ in columns])

    console.print(table)
    console.print(f"\n[green]✓ Fetched {len(data)} records[/green]")


@app.command()
def export(
    format: str = typer.Option("csv", "--format", "-f", help="Export format (csv, excel, json)"),
    output: Path = typer.Option(Path("report"), "--output", "-o", help="Output file path"),
    connector: str = typer.Option("demo", "--connector", "-c", help="Connector to export data from"),
) -> None:
    """Export cached metrics to a file."""
    settings = get_settings()
    db = Database(settings.cache_dir / "bizmetrics.db")

    data = db.get_cached_metrics(connector)

    if not data:
        console.print("[yellow]No cached data found. Run 'fetch' first.[/yellow]")
        raise typer.Exit(1)

    output_file = output.with_suffix(f".{format}" if format != "excel" else ".xlsx")

    if format == "csv":
        csv_exporter = CSVExporter()
        csv_exporter.export(data, output_file)
    elif format == "excel":
        excel_exporter = ExcelExporter()
        excel_exporter.export(data, output_file)
    else:
        console.print(f"[red]Format '{format}' not supported.[/red]")
        raise typer.Exit(1)

    console.print(f"[green]✓ Exported to {output_file}[/green]")


@app.command()
def cache(
    action: str = typer.Argument("stats", help="Cache action (stats, clear)"),
) -> None:
    """Manage the metrics cache."""
    settings = get_settings()
    db = Database(settings.cache_dir / "bizmetrics.db")

    if action == "stats":
        stats = db.get_cache_stats()
        table = Table(title="📁 Cache Statistics")
        table.add_column("Connector")
        table.add_column("Records")
        table.add_column("Last Updated")

        for connector, count, updated in stats:
            table.add_row(connector, str(count), updated)

        console.print(table)
    elif action == "clear":
        db.clear_cache()
        console.print("[green]✓ Cache cleared[/green]")
    else:
        console.print(f"[red]Unknown action: {action}[/red]")


@app.command()
def config(
    show: bool = typer.Option(False, "--show", "-s", help="Show current configuration"),
) -> None:
    """Manage configuration."""
    settings = get_settings()

    if show:
        table = Table(title="⚙️ Configuration")
        table.add_column("Setting")
        table.add_column("Value")

        table.add_row("Cache Directory", str(settings.cache_dir))
        table.add_row("Log Level", settings.log_level)
        table.add_row("Default Format", settings.default_format)

        console.print(table)
    else:
        console.print("Use --show to display current configuration")


if __name__ == "__main__":
    app()
