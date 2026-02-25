import pandas as pd

from typing import Any
from datetime import date
from enum import Enum

from models import Task

# ===== HELPER ==================================================
def get_meta() -> dict[str, dict[str, Any]]:
    fields = Task.model_fields
    meta = {}
    for name, field in fields.items():
        metadata = field.json_schema_extra
        meta[name] = metadata
    return meta

def get_display_spec() -> list[tuple[str, str, str]]:
    meta = get_meta()
    return [
        (
            field,
            label.get('label', ''),
            label.get('align', 'center'),
            label.get('width', 10)
        ) 
        for field, label in meta.items()
    ] + [('days_left', 'Days left', 'center', 13)]

def get_fields() -> list[str]:
    return list(get_meta().keys())

def get_labels() -> list[str]:
    meta = get_meta()
    return [label.get('label', '') for _, label in meta.items()]

def serialize_value(value: Any) -> str:
    if value is None:
        return ''
    if isinstance(value, Enum):
        return str(value.value)
    if isinstance(value, date):
        return value.strftime('%Y-%m-%d')
    return str(value)

def from_storage(df: pd.DataFrame) -> list[Task]:
    df.columns = get_fields()
    df = df.replace({pd.NA : None})
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
        fields = get_fields()
        df = pd.DataFrame(columns=fields)
    else:
        df = pd.DataFrame(rows)
    df.columns = get_labels()
    return df

def to_display(task: Task) -> dict:
    base = task.model_dump()
    base['days_left'] = task.days_left
    return {
        field: serialize_value(value)
        for field, value in base.items()
    }