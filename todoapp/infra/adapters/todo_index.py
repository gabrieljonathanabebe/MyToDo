from typing import Any

from todoapp.domain.models import ToDoListItem


def from_storage(data: list[dict[str, Any]]) -> list[ToDoListItem]:
    return [ToDoListItem.model_validate(item) for item in data]

def to_storage(items: list[ToDoListItem]) -> list[dict[str, Any]]:
    return [item.model_dump(mode='json') for item in items]