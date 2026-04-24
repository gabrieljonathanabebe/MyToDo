# tests/test_service.py

from mytodo.core.results import Code
from mytodo.domain.todo_list import ToDoList
from mytodo.core.services import ToDoService, TaskService
from tests.fakes import FakeRepo


# ===== TODO SERVICE =====================================================
def test_get_todos_returns_ok_and_data(
    todo_service: ToDoService, repo: FakeRepo
) -> None:
    todo = ToDoList.create_new("Existing To-Do")
    repo.save_todo(todo)
    repo.register_todo_summary(todo)

    res = todo_service.get_todos()

    assert res.code == Code.OK
    assert res.data is not None
    assert len(res.data) == 1


def test_create_todo_success_returns_created_and_data(
    todo_service: ToDoService,
) -> None:
    res = todo_service.create_todo("New To-Do")

    assert res.code == Code.CREATED
    assert res.data is not None


def test_create_todo_duplicate_returns_already_exists(
    todo_service: ToDoService, repo: FakeRepo
) -> None:
    todo = ToDoList.create_new("New To-Do")
    repo.save_todo(todo)
    repo.register_todo_summary(todo)

    res = todo_service.create_todo("New To-Do")

    assert res.code == Code.ALREADY_EXISTS
    assert res.data is None


def test_open_todo_success_returns_ok_and_data(
    todo_service: ToDoService, repo: FakeRepo
) -> None:
    todo = ToDoList.create_new("Existing To-Do")
    repo.save_todo(todo)
    repo.register_todo_summary(todo)

    res = todo_service.open_todo(todo.id)

    assert res.code == Code.OK
    assert res.data is not None
    assert res.data.id == todo.id


def test_open_todo_missing_returns_not_found(todo_service: ToDoService) -> None:
    res = todo_service.open_todo("missing-id")

    assert res.code == Code.NOT_FOUND
    assert res.data is None


def test_delete_todo_success_returns_ok(
    todo_service: ToDoService, repo: FakeRepo
) -> None:
    todo = ToDoList.create_new("Delete Me")
    repo.save_todo(todo)
    repo.register_todo_summary(todo)

    res = todo_service.delete_todo(todo.id)

    assert res.code == Code.OK
    assert res.data is None


def test_delete_todo_missing_returns_not_found(todo_service: ToDoService) -> None:
    res = todo_service.delete_todo("missing-id")

    assert res.code == Code.NOT_FOUND
    assert res.data is None


# ===== TASK SERVICE =====================================================
def test_create_task_success_returns_created_and_data(
    task_service: TaskService,
) -> None:
    todo = ToDoList.create_new("Test")

    res = task_service.create_task(
        todo,
        description="Test Desc",
        priority="2",
        due="2026-07-01",
        notes="Important",
    )

    assert res.code == Code.CREATED
    assert res.data is not None
    assert res.data.description == "Test Desc"


def test_delete_task_success_returns_ok(
    task_service: TaskService, todo_with_five_tasks: ToDoList
) -> None:
    task_id = todo_with_five_tasks.tasks[0].id

    res = task_service.delete_task(todo_with_five_tasks, task_id)

    assert res.code == Code.OK
    assert res.data is None


def test_delete_task_missing_returns_not_found(
    task_service: TaskService, todo_with_five_tasks: ToDoList
) -> None:
    res = task_service.delete_task(todo_with_five_tasks, "missing-id")

    assert res.code == Code.NOT_FOUND
    assert res.data is None


def test_toggle_status_success_returns_ok(
    task_service: TaskService, todo_with_five_tasks: ToDoList
) -> None:
    task_id = todo_with_five_tasks.tasks[0].id

    res = task_service.toggle_status(todo_with_five_tasks, task_id)

    assert res.code == Code.OK
    assert res.data is None


def test_toggle_status_missing_returns_not_found(
    task_service: TaskService, todo_with_five_tasks: ToDoList
) -> None:
    res = task_service.toggle_status(todo_with_five_tasks, "missing-id")

    assert res.code == Code.NOT_FOUND
    assert res.data is None


def test_sort_tasks_success_returns_ok(
    task_service: TaskService, todo_with_five_tasks: ToDoList
) -> None:
    res = task_service.sort_tasks(todo_with_five_tasks, key="due", reverse=False)

    assert res.code == Code.OK
    assert res.data is None


def test_sort_tasks_invalid_key_returns_invalid_input(
    task_service: TaskService, todo_with_five_tasks: ToDoList
) -> None:
    res = task_service.sort_tasks(todo_with_five_tasks, key="invalid", reverse=False)

    assert res.code == Code.INVALID_INPUT
    assert res.data is None


def test_update_task_description_success_returns_ok(
    task_service: TaskService, todo_with_five_tasks: ToDoList
) -> None:
    task_id = todo_with_five_tasks.tasks[0].id

    res = task_service.update_task_description(
        todo_with_five_tasks,
        task_id,
        "Updated description",
    )

    assert res.code == Code.OK
    assert res.data is None


def test_update_task_description_missing_returns_not_found(
    task_service: TaskService, todo_with_five_tasks: ToDoList
) -> None:
    res = task_service.update_task_description(
        todo_with_five_tasks,
        "missing-id",
        "Updated description",
    )

    assert res.code == Code.NOT_FOUND
    assert res.data is None


def test_update_task_status_invalid_status_returns_invalid_input(
    task_service: TaskService, todo_with_five_tasks: ToDoList
) -> None:
    task_id = todo_with_five_tasks.tasks[0].id

    res = task_service.update_task_status(
        todo_with_five_tasks,
        task_id,
        "invalid-status",
    )

    assert res.code == Code.INVALID_INPUT
    assert res.data is None
