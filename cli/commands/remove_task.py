from cleo.commands.command import Command
from cleo.helpers import argument
from domain.store import store


class RemoveTaskCommand(Command):
    name = "remove"
    description = "Removes a task from the task list"
    arguments = [
        argument("id", description="ID of task to remove", optional=False),
    ]

    def handle(self):
        task_id = int(self.argument("id"))
        store.remove_task(task_id)
        self.line(f"Removed task {task_id}")
