# BizMetrics CLI

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)
[![Type checked: mypy](https://img.shields.io/badge/type%20checked-mypy-blue.svg)](https://mypy-lang.org/)
[![CI/CD](https://github.com/gabrielsbrana/bizmetrics-cli/actions/workflows/ci.yml/badge.svg)](https://github.com/gabrielsbrana/bizmetrics-cli/actions)

A professional **Business Intelligence CLI tool** that unifies data extraction from multiple marketing platforms into a single, automated workflow.

Built for Data Analysts and Developers who are tired of manual exports.

## ✨ Features

- 📊 **Multi-source Connectors**:
  - **Google Analytics 4** (Demo & Production ready)
  - **Meta Ads** (Facebook/Instagram Marketing API)
  - **Demo Data** (For testing and prototyping)
- 🚀 **Automation Ready**:
  - **CI/CD Pipeline** with GitHub Actions
  - **Type Safe** (Mypy strict)
  - **Test Coverage** (Pytest)
- 💾 **Smart Storage**:
  - **SQLite Cache** to prevent API rate limits
  - **Pandas** for heavy data processing
- 📝 **Export Formats**:
  - **Excel** (.xlsx) with auto-formatting
  - **CSV** for data pipeline integration

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/gabrielsbrana/bizmetrics-cli.git
cd bizmetrics-cli

# Create virtual environment
python -m venv .venv

# Activate (Windows)
.venv\Scripts\activate
# Activate (Mac/Linux)
source .venv/bin/activate

# Install
pip install -e ".[dev]"
```

### Usage Examples

#### 1. Fetch Metrics
```powershell
# Get sample data
bizmetrics fetch demo

# Google Analytics 4
bizmetrics fetch google-analytics --start-date 2024-12-01 --end-date 2024-12-31

# Meta Ads (Facebook/Instagram)
bizmetrics fetch meta-ads --start-date 2024-12-01 --end-date 2024-12-31
```

#### 2. Export Reports
```powershell
# Export all cached data to Excel
bizmetrics export --format excel --output monthly_report

# Export specific connector data to CSV
bizmetrics export --format csv --connector meta-ads --output ads_data
```

#### 3. Manage Cache
```powershell
# View cache statistics
bizmetrics cache stats

# Clear cache
bizmetrics cache clear
```

## 🔌 Connectors Setup

### Google Analytics 4
To use real data:
1. Set `GOOGLE_APPLICATION_CREDENTIALS` env var to your Service Account JSON path.
2. The CLI will automatically switch from Demo mode to Live mode.

### Meta Ads
To use real data:
1. Set `META_ACCESS_TOKEN` and `META_AD_ACCOUNT_ID` env vars.
2. The CLI will fetch real campaign performance data.

## 🛠️ Development

This project uses a modern Python stack:

```bash
# Run tests
pytest tests/ -v

# Check types
mypy bizmetrics/

# Lint code
ruff check bizmetrics/
```

## 📁 Project Structure

```
bizmetrics-cli/
├── .github/workflows/    # CI/CD Pipelines
├── bizmetrics/
│   ├── connectors/       # GA4, Meta Ads, Demo connectors
│   ├── exporters/        # CSV, Excel logic
│   ├── cli.py            # Typer application
│   ├── db.py             # SQLite management
│   └── config.py         # Pydantic settings
├── tests/                # Pytest suite
└── README.md
```

## 👤 Author

**Gabriel Sbrana**
- Lead Developer & Data Analyst
- [GitHub Profile](https://github.com/gabrielsbrana)

---
Made with ❤️ for data-driven decisions.
