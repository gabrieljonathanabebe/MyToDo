from typing import Any

from todoapp.domain.models import ToDoMeta


def from_storage(data: list[dict[str, Any]]) -> list[ToDoMeta]:
    return [ToDoMeta.model_validate(item) for item in data]

def to_storage(items: list[ToDoMeta]) -> list[dict[str, Any]]:
    return [item.model_dump(mode='json') for item in items]