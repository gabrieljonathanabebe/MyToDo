from todoapp.core.service import ToDoService
from todoapp.domain.todo_list import ToDoList
from todoapp.core.results import Code
from tests.fakes import FakeRepo


# ===== TEST NEW TODO ==================================================
def test_new_todo_success(service: ToDoService, repo: FakeRepo) -> None:
    # act
    res = service.new_todo('New To-Do')
    # assert
    assert res.code == Code.CREATED
    assert res.data is not None
    assert res.data.title == 'New To-Do'
    assert res.data == repo.todos['New To-Do']

def test_new_todo_already_exists(
    service: ToDoService, repo: FakeRepo
) -> None:
    # arange
    repo.save_todo(ToDoList('New To-Do'))
    # act
    res = service.new_todo('New To-Do')
    # assert
    assert res.code == Code.ALREADY_EXISTS
    assert res.data is None
    assert len(repo.todos) == 1


# ===== TEST OPEN TODO ===================================================
def test_open_todo_by_choice_success(
    service: ToDoService, repo: FakeRepo
) -> None:
    # arange
    repo.save_todo(ToDoList('Existing To-Do'))
    # act
    res = service.open_todo_by_choice('1')
    # assert
    assert res.code == Code.OK
    assert res.data.title == 'Existing To-Do'

def test_open_todo_by_choice_invalid(
    service: ToDoService, repo: FakeRepo
) -> None:
    # arange
    repo.save_todo(ToDoList('Existing To-Do'))
    # act
    res = service.open_todo_by_choice('999')
    # assert
    assert res.code == Code.NOT_FOUND
    assert res.msg == 'Invalid selection.'

def test_open_todo_by_title_success(
    service: ToDoService, repo: FakeRepo
) -> None:
    # arange
    repo.save_todo(ToDoList('Existing To-Do'))
    # act
    res = service.open_todo_by_title('Existing To-Do')
    # assert
    assert res.code == Code.OK
    assert res.data.title == 'Existing To-Do'


# ===== TEST DELETE TODO =================================================
def test_delete_todo_by_choice_success(
    service: ToDoService, repo: FakeRepo
) -> None:
    # arange
    repo.save_todo(ToDoList('Deleted To-Do'))
    # act
    res = service.delete_todo_by_choice('1')
    # assert
    assert res.code == Code.OK
    assert len(repo.todos) == 0

def test_delete_todo_by_choice_invalid(
    service: ToDoService, repo: FakeRepo      
) -> None:
    # arange
    repo.save_todo(ToDoList('Deleted To-Do'))
    # act
    res = service.delete_todo_by_choice('999')
    # assert
    assert res.code == Code.INVALID_INPUT


# ===== TEST ADD TASK ====================================================
def test_add_task_success(service: ToDoService, repo: FakeRepo) -> None:
    # arange
    todo = ToDoList('Test')
    # act
    res = service.add_task(
        todo,
        description='Test Desc',
        priority=2,
        due=None
    )
    # assert
    assert res.code == Code.OK
    assert res.data is todo.tasks[0]
    assert repo.todos['Test'] is todo

def test_add_task_invalid(service: ToDoService, repo: FakeRepo) -> None:
    # arange
    todo = ToDoList('Test')
    # act
    res = service.add_task(
        todo,
        description='Test Desc',
        priority=4,
        due=None
    )
    # assert
    assert res.code == Code.INVALID_INPUT
    assert res.data is None
    assert 'Test' not in repo.todos


# ===== TEST DELETE TASK ==================================================
def test_delete_task_success(
    service: ToDoService, repo: FakeRepo, todo_with_five_tasks: ToDoList
) -> None:
    # act
    res = service.delete_task(todo_with_five_tasks, target_id='1')
    # assert
    assert res.code == Code.OK
    assert len(repo.todos['To-Do with five tasks'].tasks) == 4

def test_delete_task_missing(
    service: ToDoService, repo: FakeRepo, todo_with_five_tasks: ToDoList
) -> None:
    # act
    res = service.delete_task(todo_with_five_tasks, target_id='999')
    # assert
    assert res.code == Code.NOT_FOUND
    assert 'To-Do with five tasks' not in repo.todos

def test_delete_task_invalid(
    service: ToDoService, repo: FakeRepo, todo_with_five_tasks: ToDoList       
) -> None:
    # act
    res = service.delete_task(todo_with_five_tasks, target_id='abc')
    # assert
    assert res.code == Code.INVALID_INPUT
    assert 'To-Do with five tasks' not in repo.todos


# ===== TEST SORT TODO ====================================================
def test_sort_tasks_success(
    service: ToDoService, repo: FakeRepo, todo_with_five_tasks: ToDoList  
) -> None:
    # act
    res = service.sort_tasks(todo_with_five_tasks, key='due', reverse=False)
    # assert
    assert res.code == Code.OK
    assert 'To-Do with five tasks' in repo.todos

def test_sort_tasks_invalid(
    service: ToDoService, repo: FakeRepo, todo_with_five_tasks: ToDoList  
) -> None:
    # act
    res = service.sort_tasks(
        todo_with_five_tasks, key='Invalid', reverse=False
    )
    # assert
    assert res.code == Code.INVALID_INPUT
    assert 'To-Do with five tasks' not in repo.todos


# ===== TEST TOGGLE STATUS =================================================
def test_toggle_status_success(
    service: ToDoService, repo: FakeRepo, todo_with_five_tasks: ToDoList
) -> None:
    # act
    res = service.toggle_status(todo_with_five_tasks, task_id='3')
    # assert
    assert res.code == Code.OK
    assert 'To-Do with five tasks' in repo.todos

def test_toggle_status_missing(
    service: ToDoService, repo: FakeRepo, todo_with_five_tasks: ToDoList
) -> None:
    # act
    res = service.toggle_status(todo_with_five_tasks, task_id='999')
    # assert
    assert res.code == Code.NOT_FOUND
    assert 'To-Do with five tasks' not in repo.todos

def test_toggle_status_invalid(
    service: ToDoService, repo: FakeRepo, todo_with_five_tasks: ToDoList
) -> None:
    # act
    res = service.toggle_status(todo_with_five_tasks, task_id='abc')
    # assert
    assert res.code == Code.INVALID_INPUT
    assert 'To-Do with five tasks' not in repo.todos


# ===== TEST ASSIGN NEW IDS =================================================
def test_assign_new_ids(
    service: ToDoService, repo: FakeRepo, todo_with_five_tasks: ToDoList
) -> None:
    # act
    res = service.assign_new_ids(todo_with_five_tasks)
    assert res.code == Code.OK
    assert 'To-Do with five tasks' in repo.todos