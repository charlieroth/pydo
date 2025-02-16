from domain.models import Task
from domain.exceptions import TaskNotFoundException
from pydantic import BaseModel
import json


class Store(BaseModel):
    tasks: list[Task] = []

    def save(self):
        with open("tasks.json", "w") as f:
            json.dump(self.model_dump(), f, indent=4)

    def load(self):
        try:
            with open("tasks.json", "r") as f:
                data = json.load(f)
                for task in data["tasks"]:
                    t = Task(**task)
                    self.tasks.append(t)
        except FileNotFoundError:
            pass

    def get_task(self, task_id: int) -> Task:
        for task in self.tasks:
            if task.id == task_id:
                return task
        raise TaskNotFoundException(task_id)

    def add_task(self, task: Task) -> Task:
        self.tasks.append(task)
        self.save()
        return task

    def complete_task(self, task_id: int) -> Task:
        for task in self.tasks:
            if task.id == task_id:
                task.done = True
                self.save()
                return task
        raise TaskNotFoundException(task_id)

    def incomplete_task(self, task_id: int) -> Task:
        for task in self.tasks:
            if task.id == task_id:
                task.done = False
                self.save()
                return task
        raise TaskNotFoundException(task_id)

    def list_tasks(self) -> list[Task]:
        return self.tasks

    def remove_task(self, task_id: int) -> Task:
        removed_task: Task = None
        task_found = False
        for task in self.tasks:
            if task.id == task_id:
                removed_task = task
                task_found = True
                break

        if not task_found:
            raise TaskNotFoundException(task_id)

        self.tasks = [task for task in self.tasks if task.id != task_id]
        self.save()
        return removed_task


store = Store()
