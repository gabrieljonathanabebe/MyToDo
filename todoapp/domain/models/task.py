from datetime import date, datetime, timedelta
from typing import Optional
from enum import Enum

from pydantic import BaseModel, field_validator, ConfigDict


class Priority(int, Enum):
    low = 1
    medium = 2
    high = 3


class Status(str, Enum):
    open = "open"
    done = "done"
    cancelled = "cancelled"


class Task(BaseModel):
    model_config = ConfigDict(validate_assignment=True)

    id: str
    description: str
    priority: Priority
    status: Status = Status.open
    due: Optional[date] = None
    created_at: datetime
    updated_at: datetime
    completed_at: datetime | None = None
    notes: str | None = None

    @property
    def days_left(self) -> Optional[int]:
        if self.due is None:
            return None
        return (self.due - date.today()).days

    @property
    def lead_time(self) -> timedelta | None:
        if self.completed_at is None:
            return None
        return self.completed_at - self.created_at

    @property
    def lead_time_seconds(self) -> int | None:
        delta = self.lead_time
        if delta is None:
            return None
        return int(delta.total_seconds())

    @field_validator("description")
    def validate_description(cls, desc: str) -> str:
        if not desc.strip():
            raise ValueError("Description must not be empty.")
        return desc
