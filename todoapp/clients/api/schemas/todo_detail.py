# todoapp/clients/api/schemas/todo_detail.py

from datetime import date
from pydantic import BaseModel

from todoapp.domain.models import Priority, Status


# ===== REQUESTS ==============================================================
class CreateTaskRequest(BaseModel):
    description: str
    priority: Priority
    due: date | None = None


class UpdateTaskStatusRequest(BaseModel):
    status: Status


# ===== RESPONSES =============================================================
class TaskResponse(BaseModel):
    id: int
    description: str
    priority: str
    status: str
    due: date | None = None
    days_left: int | None = None


class ToDoDetailResponse(BaseModel):
    id: str
    title: str
    tasks: list[TaskResponse]