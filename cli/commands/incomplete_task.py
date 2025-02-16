from cleo.commands.command import Command
from cleo.helpers import argument
from domain.store import store


class IncompleteTaskCommand(Command):
    name = "incomplete"
    description = "Marks a task as incomplete"
    arguments = [
        argument("id", description="ID of task to mark as incomplete", optional=False),
    ]

    def handle(self):
        try:
            task_id = int(self.argument("id"))
            store.incomplete_task(task_id)
        except ValueError as e:
            self.line(str(e))
