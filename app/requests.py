from pydantic import BaseModel


class AddTaskRequest(BaseModel):
    title: str
