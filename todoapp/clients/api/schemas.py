from datetime import datetime, date

from pydantic import BaseModel


class CreateToDoRequest(BaseModel):
    title: str


class ToDoResponse(BaseModel):
    title: str


class ToDoListItemResponse(BaseModel):
    id: str
    title: str
    created_at: datetime


class TaskResponse(BaseModel):
    id: int
    description: str
    priority: int
    status: str
    due: date | None = None
    days_left: int | None = None


class ToDoDetailResponse(BaseModel):
    title: str
    tasks: list[TaskResponse]


class CreateTaskRequest(BaseModel):
    description: str
    priority: int
    due: date | None = None