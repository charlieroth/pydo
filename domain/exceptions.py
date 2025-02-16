class TaskNotFoundException(Exception):
    def __init__(self, task_id: int):
        self.message = f"Task with ID {task_id} not found"
        super().__init__(self.message)
