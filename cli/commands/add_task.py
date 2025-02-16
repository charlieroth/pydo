from cleo.commands.command import Command
from cleo.helpers import argument
from domain.models import Task
from domain.store import store


class AddTaskCommand(Command):
    name = "add"
    description = "Add a new task to the list"
    arguments = [
        argument("title", description="The title of the task", optional=False),
    ]

    def handle(self):
        title = self.argument("title")
        task = Task(id=len(store.tasks) + 1, title=title)
        store.add_task(task)
        self.line(f"Added {task.title}")
