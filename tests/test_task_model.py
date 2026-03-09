from datetime import date, timedelta

import pytest
from pydantic import ValidationError

from todoapp.domain.models import Task, Status, Priority


def test_task_defaults_status_to_open_and_due_to_none() -> None:
    task = Task(
        id=1,
        description='Test task',
        priority=Priority.medium
    )
    assert task.status == Status.open
    assert task.due is None

def test_task_days_left_returns_none_when_due_is_none() -> None:
    task = Task(
        id=1,
        description='Test task',
        priority=Priority.medium
    )
    assert task.days_left is None

def test_task_days_left_returns_day_difference_when_due_is_set() -> None:
    task = Task(
        id=1,
        description='Test task',
        priority=Priority.medium,
        due=date.today() + timedelta(days=5)
    )
    assert task.days_left == 5


# ===== VALIDATION ERRORS ==================================================
def test_task_description_must_not_be_empty() -> None:
    with pytest.raises(ValidationError):
        Task(
            id=1,
            description='',
            priority=2
        )

def test_task_description_must_not_be_whitespace() -> None:
    with pytest.raises(ValidationError):
        Task(
            id=1,
            description= '  ',
            priority=2
        )

def test_task_priority_must_be_valid() -> None:
    with pytest.raises(ValidationError):
        Task(
            id=1,
            description='Test',
            priority=4
        )