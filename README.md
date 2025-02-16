# `pydo`

`pydo` is a Python CLI and HTTP API for managing tasks

## Project Structure

This project is structured in three layers:

- `app`: [fastapi](https://fastapi.tiangolo.com/) application serving an HTTP server as an API into the underlying task store
- `cli.py`: [typer](https://typer.tiangolo.com/) application serving as a command line API into the underlying task store
- `shared`: Shared domain logic regardless of the application entrypoint

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
└── shared/
    ├── __init__.py
    ├── exceptions.py
    ├── models.py
    └── store.py
```