# ML Core Paradigms

A minimal Python project for learning AI engineering and ML core paradigms in a dev container environment.

## Project goals

- Learn Python-based AI engineering workflows
- Run experiments and tests inside a reproducible dev container
- Keep the project structure simple and extensible for future ML work
- Practice Git-based development from a clean repository scaffold

## Stack

- Python 3.12
- VS Code dev container
- pytest for testing
- black and ruff for formatting and linting
- jupyter and ipykernel for notebook-style experimentation

## Repository layout

- `.devcontainer/devcontainer.json` — editor and container setup
- `requirements.txt` — Python dependencies
- `src/ml_core_paradigms/` — package source code
- `tests/` — pytest smoke tests
- `.gitignore` — ignores local environment and Python cache files

## Local workflow

1. Open this repo in VS Code.
2. Reopen in the dev container.
3. Install dependencies.
4. Run tests and experiments.
5. Commit changes with Git.

Example commands:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
PYTHONPATH=src python -m pytest -q
```

## Example package usage

```python
from ml_core_paradigms.sample import greet

print(greet("World"))
```

Expected output:

```text
Hello, World!
```

## Notes

This repo is intentionally lightweight so it can grow into notebook-based exploration, data work, or more advanced ML pipelines later.
