from typing import Any

from todoapp.domain.models import ToDoSummary


def from_storage(data: list[dict[str, Any]]) -> list[ToDoSummary]:
    return [ToDoSummary.model_validate(item) for item in data]

def to_storage(items: list[ToDoSummary]) -> list[dict[str, Any]]:
    return [item.model_dump(mode='json') for item in items]