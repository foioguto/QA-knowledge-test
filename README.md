# QA Knowledge Test

Projeto de automação de testes para Web e API, desenvolvido como atividade da disciplina de QA.

## Stack
- Python
- Pytest
- Requests
- Selenium
- GitHub Actions

## Escopo

### API
Automação dos principais endpoints do Swagger Petstore:
- Pet
- Store
- User

### Web
Fluxo E2E no SauceDemo:
- login
- adição de produtos ao carrinho
- checkout
- finalização da compra

## Estrutura
- `api/`: automação de API
- `web/`: automação Web
- `.github/workflows/`: pipeline CI
- `requirements.txt`: dependências
- `pytest.ini`: configuração do pytest

## Instalação
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Execução
```bash
pytest api/tests -v
pytest web/tests -v
pytest -v
```
