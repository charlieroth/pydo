# `pydo`

`pydo` is a Python CLI and HTTP API for managing tasks

## Project Structure

This project is structured in three layers:

- `app`: [fastapi](https://fastapi.tiangolo.com/) application serving an HTTP server as an API into the underlying task store
- `cli`: [typer](https://typer.tiangolo.com/) application serving as a command line API into the underlying task store
- `domain`: Shared modules which contain the domain logic regardless of the application entrypoint

```
.
├── cli.py
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── dependencies.py
│   ├── requests.py
│   └── routers/
│       └── ...
├── cli/
│   ├── commands.py/
│   │   └── ...
│   └── __init__.py
└── domain/
    ├── __init__.py
    ├── exceptions.py
    ├── models.py
    └── store.py
```