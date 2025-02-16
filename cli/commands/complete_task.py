from cleo.commands.command import Command
from cleo.helpers import argument
from domain.store import store


class CompleteTaskCommand(Command):
    name = "complete"
    description = "Marks a task as completed"
    arguments = [
        argument("id", description="ID of task to complete", optional=False),
    ]

    def handle(self):
        try:
            task_id = int(self.argument("id"))
            store.complete_task(task_id)
        except ValueError as e:
            self.line(str(e))
