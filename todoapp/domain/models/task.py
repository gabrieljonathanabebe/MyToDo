from datetime import date
from typing import Optional
from enum import Enum

from pydantic import BaseModel, Field, field_validator


class Priority(int, Enum):
    low = 1
    medium = 2
    high = 3


class Status(str, Enum):
    open = 'open'
    done = 'done'
    cancelled = 'cancelled'


class Task(BaseModel):
    id: int = Field(
        ...,
        json_schema_extra={
            'label': 'ID',
            'align': 'center',
            'width': 5,
            'prompt': False,
            'order': 1
        }
    )

    description: str = Field(
        ...,
        json_schema_extra={
            'label': 'Description',
            'align': 'left',
            'width': 25,
            'prompt': True,
            'order': 2
        }
    )

    priority: Priority = Field(
        ...,
        json_schema_extra={
            'label': 'Priority',
            'align': 'center',
            'width': 11,
            'prompt': True,
            'order': 3
        }
    )

    status: Status = Field(
        default=Status.open,
        json_schema_extra={
            'label': 'Status',
            'align': 'center',
            'width': 9,
            'prompt': False,
            'order': 4
        }
    )

    due: Optional[date] = Field(
        default=None,
        json_schema_extra={
            'label': 'Due',
            'align': 'center',
            'width': 13,
            'prompt': True,
            'order': 5
        }
    )

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