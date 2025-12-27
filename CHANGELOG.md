# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2024-12-27

### Added
- Initial release of BizMetrics CLI
- CLI commands: `fetch`, `export`, `cache`, `config`
- Demo connector with sample business metrics
- Google Analytics 4 connector (demo mode)
- Meta Ads connector (demo mode)
- CSV and Excel exporters
- SQLite-based caching with TTL
- Pydantic configuration management
- GitHub Actions CI/CD pipeline
- Full type hints (mypy strict mode)
- Ruff linting configuration

### Technical
- Python 3.10+ support
- Typer for CLI framework
- Rich for terminal UI
- Pandas for data processing
- Pytest for testing with coverage
