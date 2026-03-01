from typing import Any
from datetime import date
from enum import Enum

from todoapp.domain.models import Task
from .formatters import format_status


def serialize_display_value(value: Any) -> str:
    if value is None:
        return '-'
    if isinstance(value, Enum):
        return str(value.value)
    if isinstance(value, date):
        return value.strftime('%Y-%m-%d')
    return str(value)

def to_display_row(task: Task) -> dict[str, str]:
    base = task.model_dump()
    base['days_left'] = task.days_left
    row = {
        field: serialize_display_value(value)
        for field, value in base.items()
    }
    row['status'] = format_status(task.status)
    return row