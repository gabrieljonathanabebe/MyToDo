from datetime import date

import pytest

from todoapp.domain.todo_list import ToDoList
from todoapp.core.service import ToDoService
from todoapp.domain.models import Priority, Status
from tests.fakes import FakeRepo
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
    return ToDoList('To-Do with five tasks', tasks)


@pytest.fixture
def repo() -> FakeRepo:
    return FakeRepo()

@pytest.fixture
def service(repo: FakeRepo) -> ToDoService:
    return ToDoService(repo)