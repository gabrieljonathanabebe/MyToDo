# todoapp/infra/adapters/task.py

import pandas as pd

from typing import Any
from datetime import date, datetime, timezone
from enum import Enum
from uuid import uuid4

from todoapp.domain.models import Task


# ===== HELPER ================================================================
def _fallback_timestamp() -> datetime:
    return datetime.now(timezone.utc)


# ===== SERIALIZER ============================================================
def serialize_value(value: Any) -> str:
    if value is None:
        return ''
    if isinstance(value, Enum):
        return str(value.value)
    if isinstance(value, datetime):
        return value.isoformat()
    if isinstance(value, date):
        return value.strftime('%Y-%m-%d')
    return str(value)


# ===== STORAGE ===============================================================
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
        normalized_row = normalize_task_row(row)
        rows.append(normalized_row)
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


# ===== FALLBACK FOR TASK WITH OLD DATA MODEL =================================
def normalize_task_row(row: dict[str, Any]) -> dict[str, Any]:
    normalized = dict(row)
    raw_id = normalized.get('id')
    if raw_id is None or raw_id == '':
        normalized['id'] = str(uuid4())
    else:
        normalized['id'] = str(raw_id)
    fallback_now = _fallback_timestamp()
    if normalized.get('created_at') is None:
        normalized['created_at'] = fallback_now
    if normalized.get('updated_at') is None:
        normalized['updated_at'] = normalized['created_at']
    if normalized.get('completed_at') is None:
        normalized['completed_at'] = None
    if normalized.get('notes') is None:
        normalized['notes'] = None
    return normalized