# minha-app

Projeto-base para aprender Python com estrutura profissional.

## Como rodar

```bash
uv venv
source .venv/bin/activate
uv pip install -e ".[dev]"
make run
make test
make lint
```

## Estrutura

```
src/minha_app/   código da aplicação
tests/           testes automatizados
pyproject.toml   configuração do projeto e das ferramentas
Makefile         atalhos de comandos
```

## Próximos passos

1. Mude `saudacao()` em `src/minha_app/main.py`.
2. Escreva um teste novo em `tests/test_main.py`.
3. Rode `make test` até ficar verde.
