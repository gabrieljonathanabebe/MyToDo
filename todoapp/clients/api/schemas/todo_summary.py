# todoapp/clients/api/schemas/todo_summary.py

from datetime import datetime
from pydantic import BaseModel


# ===== REQUESTS ==============================================================
class CreateToDoRequest(BaseModel):
    title: str


# ===== RESPONSES =============================================================
class ToDoSummaryResponse(BaseModel):
    id: str
    title: str
    created_at: datetime
    updated_at: datetime
    task_count: int