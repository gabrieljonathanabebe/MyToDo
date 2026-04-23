# tests/test_domain_todo_list.py

from datetime import date

import pytest

from todoapp.domain.todo_list import ToDoList
from todoapp.domain.models import Status, Priority
import tests.factories as factories


# ===== CREATE TASK =====================================================
def test_create_task_adds_open_task_with_expected_values(todo_empty: ToDoList) -> None:
    task = todo_empty.create_task(
        description='Test task 1',
        priority='2',
        due='2026-05-26',
        notes='Important note',
    )

    assert len(todo_empty.tasks) == 1
    assert task.status == Status.open
    assert task.description == 'Test task 1'
    assert task.priority == Priority.medium
    assert task.due == date(2026, 5, 26)
    assert task.notes == 'Important note'
    assert task.completed_at is None


def test_create_task_appends_to_existing_list(todo_with_five_tasks: ToDoList) -> None:
    task = todo_with_five_tasks.create_task(
        description='Test task 6',
        priority='1',
        due='2026-06-09',
        notes=None,
    )

    assert len(todo_with_five_tasks.tasks) == 6
    assert task in todo_with_five_tasks.tasks


# ===== DELETE TASK =====================================================
def test_delete_existing_task_returns_true_and_removes_task(todo_with_five_tasks: ToDoList) -> None:
    task_id = todo_with_five_tasks.tasks[0].id

    result = todo_with_five_tasks.delete_task(task_id)

    assert result is True
    assert len(todo_with_five_tasks.tasks) == 4
    assert all(t.id != task_id for t in todo_with_five_tasks.tasks)


def test_delete_missing_task_returns_false(todo_with_five_tasks: ToDoList) -> None:
    result = todo_with_five_tasks.delete_task('missing-id')

    assert result is False


# ===== SORT TASKS ======================================================
def test_sort_tasks_by_due_puts_none_values_last(todo_with_five_tasks: ToDoList) -> None:
    todo_with_five_tasks.sort_tasks('due', reverse=False)

    assert todo_with_five_tasks.tasks[-1].due is None


def test_sort_tasks_keeps_same_task_set(todo_with_five_tasks: ToDoList) -> None:
    original_ids = {task.id for task in todo_with_five_tasks.tasks}

    todo_with_five_tasks.sort_tasks('priority', reverse=True)

    assert {task.id for task in todo_with_five_tasks.tasks} == original_ids


# ===== TOGGLE STATUS ===================================================
def test_toggle_status_from_open_to_done_sets_completed_at() -> None:
    task = factories.make_task(status=Status.open)
    todo = ToDoList(title='test', tasks=[task])

    old_updated_at = task.updated_at
    result = todo.toggle_status(task.id)

    assert result is True
    assert task.status == Status.done
    assert task.completed_at is not None
    assert task.updated_at >= old_updated_at


def test_toggle_status_from_done_to_open_clears_completed_at() -> None:
    task = factories.make_task(status=Status.done)
    todo = ToDoList(title='test', tasks=[task])

    old_updated_at = task.updated_at
    result = todo.toggle_status(task.id)

    assert result is True
    assert task.status == Status.open
    assert task.completed_at is None
    assert task.updated_at >= old_updated_at


def test_toggle_status_returns_false_for_missing_id() -> None:
    task = factories.make_task()
    todo = ToDoList(title='test', tasks=[task])

    result = todo.toggle_status('missing-id')

    assert result is False


# ===== UPDATE TASK =====================================================
def test_update_task_description_updates_value_and_timestamp() -> None:
    task = factories.make_task()
    todo = ToDoList(title='test', tasks=[task])

    old_updated_at = task.updated_at
    result = todo.update_task_description(task.id, 'Updated description')

    assert result is True
    assert task.description == 'Updated description'
    assert task.updated_at >= old_updated_at


def test_update_task_priority_updates_value_and_timestamp() -> None:
    task = factories.make_task(priority=Priority.low)
    todo = ToDoList(title='test', tasks=[task])

    old_updated_at = task.updated_at
    result = todo.update_task_priority(task.id, 3)

    assert result is True
    assert task.priority == Priority.high
    assert task.updated_at >= old_updated_at


def test_update_task_due_updates_value_and_timestamp() -> None:
    task = factories.make_task(due=None)
    todo = ToDoList(title='test', tasks=[task])

    old_updated_at = task.updated_at
    new_due = date(2026, 7, 1)
    result = todo.update_task_due(task.id, new_due)

    assert result is True
    assert task.due == new_due
    assert task.updated_at >= old_updated_at


@pytest.mark.parametrize(
    'method_name, args',
    [
        ('update_task_description', ('missing-id', 'Updated description')),
        ('update_task_priority', ('missing-id', 2)),
        ('update_task_due', ('missing-id', date(2026, 7, 1))),
    ],
)
def test_update_task_methods_return_false_for_missing_id(method_name: str, args: tuple) -> None:
    task = factories.make_task()
    todo = ToDoList(title='test', tasks=[task])

    result = getattr(todo, method_name)(*args)

    assert result is False