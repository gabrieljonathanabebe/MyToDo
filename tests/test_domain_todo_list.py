from datetime import date

import pytest

from todoapp.domain.todo_list import ToDoList
from todoapp.domain.models import Status


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
def test_sort_todo_by_id_or_priority_as_key(
    todo_with_five_tasks: ToDoList,
    key: str,
    reverse: bool,
    expected_ids: list[int]
) -> None:
    todo_with_five_tasks.sort_todo(key, reverse)
    sorted_ids = [t.id for t in todo_with_five_tasks.tasks]
    assert sorted_ids == expected_ids