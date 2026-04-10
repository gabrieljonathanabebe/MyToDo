from datetime import date

import pytest

from todoapp.domain.todo_list import ToDoList
from todoapp.domain.models import Status
import tests.factories as factories


# ===== NEXT ID =======================================================
def test_next_id_on_empty(todo_empty: ToDoList) -> None:
    assert todo_empty.next_id() == 1

def test_next_id_on_non_empty(todo_with_five_tasks: ToDoList) -> None:
    assert todo_with_five_tasks.next_id() == 6


# ===== ADD TASK ======================================================
def test_add_task_on_empty(todo_empty: ToDoList) -> None:
    task = todo_empty.add_task(
        description='Test task 1',
        priority=2,
        due=date(2026, 5, 26)
    )
    assert len(todo_empty.tasks) == 1
    assert task.id == 1
    assert task.status == Status.open
    assert task.description == 'Test task 1'

def test_add_task_on_non_empty(todo_with_five_tasks: ToDoList) -> None:
    task = todo_with_five_tasks.add_task(
        description='Test task 6',
        priority=1,
        due=date(2026, 6, 9)
    )
    assert len(todo_with_five_tasks.tasks) == 6
    assert task.id == 6


# ===== DELETE TASK ====================================================
def test_delete_existing_task_returns_true(
    todo_with_five_tasks: ToDoList
) -> None:
    result = todo_with_five_tasks.delete_task(1)
    assert result is True
    assert len(todo_with_five_tasks.tasks) == 4
    assert all(t.id != 1 for t in todo_with_five_tasks.tasks)

def test_delete_missing_task_returns_false(
    todo_with_five_tasks: ToDoList
) -> None:
    result = todo_with_five_tasks.delete_task(999)
    assert result is False
    assert len(todo_with_five_tasks.tasks) == 5


# ===== SORT TODO ======================================================
@pytest.mark.parametrize(
    'key, reverse, expected_ids',
    [
        ('id', False, [1, 2, 3, 4, 5]),
        ('id', True, [5, 4, 3, 2, 1]),
        ('priority', False, [3, 2, 5, 1, 4]),
        ('priority', True, [1, 4, 2, 5, 3])
    ],
    ids=['id_asc', 'id_desc', 'priority_asc', 'priority_desc']
)
def test_sort_tasks_by_id_or_priority_as_key(
    todo_with_five_tasks: ToDoList,
    key: str,
    reverse: bool,
    expected_ids: list[int]
) -> None:
    todo_with_five_tasks.sort_tasks(key, reverse)
    sorted_ids = [t.id for t in todo_with_five_tasks.tasks]
    assert sorted_ids == expected_ids


@pytest.mark.parametrize(
    'key, reverse, expected_ids',
    [
        ('due', False, [3, 1, 4, 2, 5]),
        ('due', True, [1, 4, 3, 2, 5])
    ],
    ids=['due_asc', 'due_desc']
)
def test_sort_tasks_by_due_as_key(
    todo_with_five_tasks: ToDoList,
    key: str,
    reverse: bool,
    expected_ids: list[int]
) -> None:
    todo_with_five_tasks.sort_tasks(key, reverse)
    sorted_ids = [t.id for t in todo_with_five_tasks.tasks]
    assert sorted_ids == expected_ids


# ===== ASSIGN NEW IDS ==================================================
def test_assign_new_ids(todo_with_five_tasks: ToDoList) -> None:
    todo_with_five_tasks.delete_task(1)
    count = todo_with_five_tasks.assign_new_ids()
    new_ids = [t.id for t in todo_with_five_tasks.tasks]
    assert new_ids == list(range(1, 5))
    assert count == 4


# ===== TOGGLE STATUS ===================================================
@pytest.mark.parametrize(
    'start_status, expected_status',
    [
        (Status.open, Status.done),
        (Status.done, Status.open)
    ],
    ids=['toggle_done', 'toggle_open']
)
def test_toggle_status(start_status: Status, expected_status: Status) -> None:
    task = factories.make_task(status=start_status)
    todo = ToDoList('test', [task])
    result = todo.toggle_status(1)
    assert todo.tasks[0].status == expected_status
    assert result is True


def test_toggle_status_returns_false_for_missing_id() -> None:
    task = factories.make_task()
    todo = ToDoList('test', [task])
    result = todo.toggle_status(999)
    assert result is False