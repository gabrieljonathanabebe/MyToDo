from datetime import date
from typing import Optional
from enum import Enum

from pydantic import BaseModel, field_validator


class Priority(int, Enum):
    low = 1
    medium = 2
    high = 3


class Status(str, Enum):
    open = 'open'
    done = 'done'
    cancelled = 'cancelled'


class Task(BaseModel):
    id: int
    description: str
    priority: Priority
    status: Status = Status.open
    due: Optional[date] = None

    @property
    def days_left(self) -> Optional[int]:
        if self.due is None:
            return None
        return (self.due - date.today()).days

    @field_validator('description')
    def validate_description(cls, desc: str) -> str:
        if not desc.strip():
            raise ValueError('Description must not be empty.')
        return desc