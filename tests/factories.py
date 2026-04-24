# tests/factories.py

from datetime import date, datetime, timezone, timedelta
from typing import Optional
from uuid import uuid4

from mytodo.domain.models import Task, Priority, Status


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def make_task(
    id: str | None = None,
    description: str = "Test task",
    priority: Priority = Priority.low,
    status: Status = Status.open,
    due: Optional[date] = None,
    created_at: datetime | None = None,
    updated_at: datetime | None = None,
    completed_at: datetime | None = None,
    notes: str | None = None,
) -> Task:
    created_at = created_at or utc_now()
    updated_at = updated_at or created_at

    if status == Status.done and completed_at is None:
        completed_at = created_at + timedelta(hours=2)

    return Task(
        id=id or str(uuid4()),
        description=description,
        priority=priority,
        status=status,
        due=due,
        created_at=created_at,
        updated_at=updated_at,
        completed_at=completed_at,
        notes=notes,
    )


def make_tasks(
    n: int,
    priorities: Optional[list[Priority]] = None,
    statuses: Optional[list[Status]] = None,
    dues: Optional[list[Optional[date]]] = None,
) -> list[Task]:
    if priorities is not None and len(priorities) == 0:
        raise ValueError("Priorities must be None or a non-empty list")
    if statuses is not None and len(statuses) == 0:
        raise ValueError("Statuses must be None or a non-empty list")
    if dues is not None and len(dues) == 0:
        raise ValueError("Dues must be None or a non-empty list")

    tasks: list[Task] = []

    for i in range(n):
        priority = (
            Priority.low if priorities is None else priorities[i % len(priorities)]
        )
        status = Status.open if statuses is None else statuses[i % len(statuses)]
        due = None if dues is None else dues[i % len(dues)]

        tasks.append(
            make_task(
                description=f"Test task {i + 1}",
                priority=priority,
                status=status,
                due=due,
            )
        )

    return tasks
