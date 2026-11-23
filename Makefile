PYTHON ?= python3

.PHONY: install test lint format run clean

install:
	$(PYTHON) -m pip install -e ".[dev]"

test:
	$(PYTHON) -m pytest

lint:
	$(PYTHON) -m ruff check .

format:
	$(PYTHON) -m ruff format .

run:
	$(PYTHON) -m minha_app

clean:
	rm -rf .pytest_cache .mypy_cache .ruff_cache build dist *.egg-info
