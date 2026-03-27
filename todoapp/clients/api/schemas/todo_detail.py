# todoapp/clients/api/schemas/todo_detail.py

from datetime import date
from pydantic import BaseModel


# ===== REQUESTS ==============================================================
class CreateTaskRequest(BaseModel):
    description: str
    priority: int
    due: date | None = None


# ===== RESPONSES =============================================================
class TaskResponse(BaseModel):
    id: int
    description: str
    priority: int
    status: str
    due: date | None = None
    days_left: int | None = None

class ToDoDetailResponse(BaseModel):
    id: str
    title: str
    tasks: list[TaskResponse]