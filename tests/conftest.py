# tests/conftest.py

from datetime import date

import pytest

from mytodo.domain.todo_list import ToDoList
from mytodo.core.services import ToDoService, TaskService
from mytodo.domain.models import Priority, Status
from tests.fakes import FakeRepo
import tests.factories as factories


@pytest.fixture
def todo_empty() -> ToDoList:
    return ToDoList.create_new("To-Do empty")


@pytest.fixture
def todo_with_five_tasks() -> ToDoList:
    tasks = factories.make_tasks(
        n=5,
        priorities=[Priority.high, Priority.medium, Priority.low],
        statuses=[Status.open, Status.open, Status.done],
        dues=[date(2026, 5, 11), None, date(2026, 4, 1)],
    )

    todo = ToDoList.create_new("To-Do with five tasks")
    todo.tasks = tasks
    return todo


@pytest.fixture
def repo() -> FakeRepo:
    return FakeRepo()


@pytest.fixture
def todo_service(repo: FakeRepo) -> ToDoService:
    return ToDoService(repo)


@pytest.fixture
def task_service(repo: FakeRepo) -> TaskService:
    return TaskService(repo)
