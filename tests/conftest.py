from datetime import date

import pytest

from todoapp.domain.todo_list import ToDoList
from todoapp.domain.models import Task, Priority, Status
import tests.factories as factories


@pytest.fixture
def todo_empty() -> ToDoList:
    return ToDoList('To-Do empty')

@pytest.fixture
def todo_with_five_tasks() -> ToDoList:
    tasks = factories.make_tasks(
        n=5,
        priorities=[Priority.high, Priority.medium, Priority.low],
        statuses=[Status.open, Status.open, Status.done],
        dues=[date(2026, 5, 11), None, date(2026, 4, 1)]
    )
    return ToDoList('To-Do with tasks', tasks)