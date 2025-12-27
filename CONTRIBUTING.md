# 🤝 Contributing to BizMetrics CLI

Thank you for your interest in contributing to BizMetrics CLI!

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/gabrielsbrana/bizmetrics-cli.git
cd bizmetrics-cli

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# or
.venv\Scripts\activate  # Windows

# Install dev dependencies
pip install -e ".[dev]"
```

## 🧪 Running Tests

```bash
# All tests with coverage
pytest tests/ -v --cov=bizmetrics

# Just connectors
pytest tests/test_connectors.py -v
```

## ✅ Code Quality

Before submitting, ensure:

```bash
# Lint check
ruff check bizmetrics/

# Type check
mypy bizmetrics/ --ignore-missing-imports

# Format
ruff format bizmetrics/
```

## 📝 Pull Request Process

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Make changes and add tests
4. Ensure all checks pass
5. Commit (`git commit -m 'feat: Add amazing feature'`)
6. Push (`git push origin feature/amazing-feature`)
7. Open Pull Request

## 📋 Commit Convention

We use [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation
- `refactor:` Code refactoring
- `test:` Adding tests
- `chore:` Maintenance

## 🎯 Areas to Contribute

- [ ] New connectors (HubSpot, Salesforce, LinkedIn Ads)
- [ ] PDF exporter
- [ ] Dashboard TUI
- [ ] Documentation improvements
- [ ] Test coverage

## 📄 License

By contributing, you agree that your contributions will be licensed under MIT.
