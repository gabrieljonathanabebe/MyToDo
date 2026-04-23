# tests/test_task_model.py

from datetime import date, timedelta, datetime, timezone

import pytest
from pydantic import ValidationError

from todoapp.domain.models import Task, Status, Priority
import tests.factories as factories


# ===== DEFAULTS ==============================================================
def test_task_defaults_status_due_completed_at_notes() -> None:
    task = factories.make_task()
    assert task.status == Status.open
    assert task.due is None
    assert task.completed_at is None
    assert task.notes is None


# ===== DAYS LEFT =============================================================
def test_task_days_left_returns_none_when_due_is_none() -> None:
    task = factories.make_task(due=None)
    assert task.days_left is None

def test_task_days_left_returns_day_diff_when_due_is_set() -> None:
    task = factories.make_task(due=date.today() + timedelta(days=5))
    assert task.days_left == 5


# ===== LEAD TIME =============================================================
def test_task_lead_time_returns_none_when_task_is_not_completed() -> None:
    task = factories.make_task(status=Status.open, completed_at=None)
    assert task.lead_time is None
    assert task.lead_time_seconds is None

def test_task_lead_time_returns_timedelta_when_task_is_completed() -> None:
    created_at = datetime(2027, 1, 1, 10, 0, tzinfo=timezone.utc)
    completed_at = datetime(2027, 1, 1, 12, 30, tzinfo=timezone.utc)
    task = factories.make_task(
        status=Status.done,
        created_at=created_at,
        updated_at=completed_at,
        completed_at=completed_at
    )
    assert task.lead_time == timedelta(hours=2, minutes=30)
    assert task.lead_time_seconds == 9000


# ===== VALIDATION ERRORS ==================================================
def test_task_description_must_not_be_empty() -> None:
    with pytest.raises(ValidationError):
        Task(
            id='test-id',
            description='',
            priority=Priority.medium,
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc)
        )

def test_task_description_must_not_be_whitespace() -> None:
    with pytest.raises(ValidationError):
        Task(
            id='test-id',
            description= '  ',
            priority=Priority.medium,
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc)
        )

def test_task_priority_must_be_valid() -> None:
    with pytest.raises(ValidationError):
        Task(
            id='test-id',
            description='Test',
            priority=4,
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc)
        )