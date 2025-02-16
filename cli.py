import typer
from rich import print
from rich.console import Console
from rich.table import Table
from domain.models import Task
from domain.store import store

console = Console()
app = typer.Typer()


def print_tasks(tasks: list[Task]):
    table = Table("ID", "Title", "Done", title="Tasks")
    for task in tasks:
        if task.done:
            table.add_row(str(task.id), task.title, "[green]✓[/green]")
        else:
            table.add_row(str(task.id), task.title, "[red]✗[/red]")

    console.print(table)


@app.command()
def add(title: str):
    task = Task(id=len(store.tasks) + 1, title=title)
    store.add_task(task)
    print(f"Added {task.title}")


@app.command()
def list():
    tasks = store.list_tasks()
    print_tasks(tasks)


@app.command()
def remove(task_id: int):
    store.remove_task(task_id)
    print(f"[green]✓[/green] removed {task_id}")
    print_tasks(store.list_tasks())


@app.command()
def did(task_id: int):
    store.complete_task(task_id)
    print(f"[green]✓[/green] did {task_id}")
    print_tasks(store.list_tasks())


@app.command()
def undo(task_id: int):
    store.incomplete_task(task_id)
    print(f"Completed task {task_id}")
    print(f"[green]✓[/green] undid {task_id}")
    print_tasks(store.list_tasks())


def main():
    store.load()
    app()


if __name__ == "__main__":
    main()
