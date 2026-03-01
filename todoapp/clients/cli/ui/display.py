from typing import Any
from datetime import date
from enum import Enum

from todoapp.domain.models import Task
from . import display_spec
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
    row = {}
    for field in display_spec.get_fields():
        value = base.get(field)
        formatter = display_spec.get_formatter(field)
        if formatter:
            row[field] = formatter(getattr(task, field))
        else:
            row[field] = serialize_display_value(value)
    return row