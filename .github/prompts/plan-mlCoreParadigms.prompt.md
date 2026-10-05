# Plan: Python AI Engineering Learning Project

## Goal
Create a Python-based dev container project for learning AI engineering paradigms, with a lightweight structure for running Python experiments, adding tests, and working in Git.

## Scope
- Set up a dev container that supports Python development in VS Code
- Make it easy to run Python scripts and tests locally inside the container
- Keep the repo ready for Git commits and pushes
- Use a minimal, extensible project layout that can grow into ML/data science work later

## Recommended stack
- Python 3.12
- VS Code dev container
- Git support in the container
- pytest for testing
- black and ruff for formatting and linting
- ipykernel and jupyter for notebook-style experimentation

## Project structure
- .devcontainer/
  - devcontainer.json
- requirements.txt
- src/
  - ml_core_paradigms/
    - __init__.py
    - sample.py
- tests/
  - test_smoke.py
- .gitignore
- README.md

## Dev container configuration
Use a Python dev container image and install standard Python tooling on container creation.

Example devcontainer.json:

```json
{
  "name": "ml-core-paradigms",
  "image": "mcr.microsoft.com/devcontainers/python:1-3.12-bookworm",
  "features": {
    "ghcr.io/devcontainers/features/git:1": {}
  },
  "postCreateCommand": "python -m pip install --upgrade pip && python -m pip install pytest black ruff ipykernel jupyter",
  "customizations": {
    "vscode": {
      "settings": {
        "python.defaultInterpreterPath": "/usr/local/bin/python",
        "python.testing.pytestEnabled": true,
        "python.testing.pytestArgs": ["tests"]
      },
      "extensions": [
        "ms-python.python",
        "ms-python.vscode-pylance",
        "ms-python.black-formatter",
        "charliermarsh.ruff"
      ]
    }
  },
  "remoteUser": "vscode"
}
```

## Dependencies
Suggested requirements.txt:

```txt
pytest==8.3.3
black==24.8.0
ruff==0.6.9
ipykernel==6.29.5
jupyter==1.1.1
```

## Python project layout
Keep the package focused and simple for learning patterns, for example:

- `src/ml_core_paradigms/__init__.py`
- `src/ml_core_paradigms/sample.py`
- `tests/test_smoke.py`

Example sample module:

```python
from __future__ import annotations


def greet(name: str) -> str:
    return f"Hello, {name}!"
```

Example smoke test:

```python
from ml_core_paradigms.sample import greet


def test_greet():
    assert greet("World") == "Hello, World!"
```

## Typical workflow
1. Open the repo in VS Code
2. Reopen in the dev container
3. Create or activate a virtual environment if needed
4. Install dependencies
5. Run tests with pytest
6. Commit changes to Git
7. Push to a remote repository

Example commands:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pytest -q
git status
git add .
git commit -m "Initial project setup"
git push origin main
```

## Why this plan works
- It gives a reproducible environment for learning
- It supports Python code execution and tests directly in the editor
- It is minimal enough to avoid unnecessary setup overhead
- It is extensible as the project grows into data science or AI engineering topics

## Next refinement areas
- Add a basic package structure for notebooks and experiments
- Add a data folder for learning examples
- Add a patterns folder for ML pipeline exercises
- Add a README with step-by-step tutorials and project goals
