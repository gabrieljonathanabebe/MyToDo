# todoapp/clients/cli/ui/adapters/base.py

from typing import Any
from enum import Enum
from datetime import date

from pydantic import BaseModel

from todoapp.clients.cli.ui.specs import TableSpec


def to_display_value(value: Any) -> str:
    if value is None:
        return "-"
    if isinstance(value, Enum):
        return str(value.value)
    if isinstance(value, date):
        return value.strftime("%Y-%m-%d")
    return str(value)


def to_display_row(obj: BaseModel, spec: TableSpec) -> dict[str, str]:
    base = obj.model_dump()
    row = {}
    for field in spec.fields:
        value = base.get(field)
        formatter = spec.formatter(field)
        if formatter:
            row[field] = formatter(value)
        else:
            row[field] = to_display_value(value)
    return row
