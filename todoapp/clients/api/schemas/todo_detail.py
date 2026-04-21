# todoapp/clients/api/schemas/todo_detail.py

from datetime import date, datetime
from pydantic import BaseModel

from todoapp.domain.models import Priority, Status


# ===== REQUESTS ==============================================================
class CreateTaskRequest(BaseModel):
    description: str
    priority: Priority
    due: date | None = None
    notes: str | None = None

class UpdateTaskStatusRequest(BaseModel):
    status: Status


class SortTasksRequest(BaseModel):
    key: str
    reverse: bool = False


class UpdateTaskDescriptionRequest(BaseModel):
    description: str


class UpdateTaskPriorityRequest(BaseModel):
    priority: int


class UpdateTaskDueRequest(BaseModel):
    due: date | None = None


# ===== RESPONSES =============================================================
class TaskResponse(BaseModel):
    id: str
    description: str
    priority: str
    status: str
    due: date | None = None
    days_left: int | None = None
    created_at: datetime
    updated_at: datetime
    completed_at: datetime | None = None
    notes: str | None
    lead_time_seconds: int | None = None


class ToDoDetailResponse(BaseModel):
    id: str
    title: str
    tasks: list[TaskResponse]