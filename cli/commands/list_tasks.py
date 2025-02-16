from cleo.commands.command import Command
from domain.store import store


class ListTasksCommand(Command):
    name = "list"
    description = "Add a new task to the list"

    def handle(self):
        self.line("Tasks:")
        tasks = store.list_tasks()
        for task in tasks:
            if task.done:
                self.line(f"[x] {task.title}")
            else:
                self.line(f"[ ] {task.title}")
