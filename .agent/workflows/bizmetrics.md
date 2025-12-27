# BizMetrics CLI - Workflow de Uso

## Instalação Rápida

```powershell
// turbo
cd "c:\Users\Gabriel\Downloads\zyspotify-master\bizmetrics-cli"
.venv\Scripts\activate
```

## Comandos Principais

### 1. Buscar Métricas
```powershell
// turbo
bizmetrics fetch demo
bizmetrics fetch google-analytics --start-date 2024-12-01 --end-date 2024-12-31
bizmetrics fetch meta-ads -s 2024-12-20 -e 2024-12-27
```

### 2. Exportar Dados
```powershell
// turbo
bizmetrics export --format excel --output relatorio
bizmetrics export --format csv --output dados --connector meta-ads
```

### 3. Gerenciar Cache
```powershell
// turbo
bizmetrics cache stats
bizmetrics cache clear
```

### 4. Ver Configurações
```powershell
// turbo
bizmetrics config --show
```

## Desenvolvimento

### Rodar Testes
```powershell
// turbo
pytest tests/ -v
```

### Verificar Lint
```powershell
// turbo
ruff check bizmetrics/
```

### Verificar Types
```powershell
// turbo
mypy bizmetrics/ --ignore-missing-imports
```

### Commit e Push
```powershell
git add .
git commit -m "feat: descrição"
git push origin main
```
