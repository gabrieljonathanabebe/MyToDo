from typing import Optional
from datetime import date

from todoapp.domain.models import Task, Priority, Status

def make_task(
    id: int = 1,
    description: str = 'Test task',
    priority: Priority = Priority.low,
    status: Status = Status.open,
    due: Optional[date] = None,
) -> Task:
    return Task(
        id=id,
        description=f"{description} {id}",
        priority=priority,
        status=status,
        due=due,
    )

def make_tasks(
    n: int,
    start_id: int = 1,
    priorities: Optional[list[Priority]] = None,
    statuses: Optional[list[Status]] = None,
    dues: Optional[list[Optional[date]]] = None,
) -> list[Task]:
    if priorities is not None and len(priorities) == 0:
        raise ValueError('Priorities must be None or a non-empty list')
    if statuses is not None and len(statuses) == 0:
        raise ValueError('Statutes must be None or a non-empty list')
    if dues is not None and len(dues) == 0:
        raise ValueError('Dues must be None or a non-empty list')
    tasks: list[Task] = []
    for i in range(n):
        due = None if dues is None else dues[i % len(dues)]
        priority = Priority.low if priorities is None else priorities[i % len(priorities)]
        status = Status.open if statuses is None else statuses[i % len(statuses)]
        tasks.append(
            make_task(
                id=start_id + i,
                priority=priority,
                status=status,
                due=due
            )
        )
    return tasks