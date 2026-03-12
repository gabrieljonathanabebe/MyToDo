import pandas as pd

from typing import Any
from datetime import date
from enum import Enum

from todoapp.domain.models import Task

# ===== SERIALIZER ==================================================
def serialize_value(value: Any) -> str:
    if value is None:
        return ''
    if isinstance(value, Enum):
        return str(value.value)
    if isinstance(value, date):
        return value.strftime('%Y-%m-%d')
    return str(value)

# ===== STORAGE =====================================================
def from_storage(df: pd.DataFrame) -> list[Task]:
    df = df.replace({pd.NA : None})
    df.columns = [c.strip().lower() for c in df.columns]
    raw_rows = df.to_dict(orient='records')
    rows = []
    for raw_row in raw_rows:
        row = {
            key: value if pd.notna(value) else None 
            for key, value in raw_row.items()
        }
        rows.append(row)
    return [Task.model_validate(r) for r in rows]

def to_storage(tasks: list[Task]) -> pd.DataFrame:
    rows = []
    for task in tasks:
        base = task.model_dump()
        serialized = {
            field: serialize_value(value)
            for field, value in base.items()
        }
        rows.append(serialized)
    if not rows:
        fields = list(Task.model_fields.keys())
        return pd.DataFrame(columns=fields)
    return pd.DataFrame(rows)