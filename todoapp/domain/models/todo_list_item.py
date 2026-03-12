from datetime import datetime

from pydantic import BaseModel


class ToDoListItem(BaseModel):
    id: str
    title: str
    created_at: datetime