from pathlib import Path

import pytest

from todoapp.infra.csv_repository import CsvRepository
from todoapp.domain.todo_list import ToDoList
import tests.factories as factories


def test_save_and_load_roundtrip(tmp_path: Path) -> None:
    # arange
    repo = CsvRepository(tmp_path)
    tasks = factories.make_tasks(3)
    todo = ToDoList('test', tasks)
    # act
    repo.save_todo(todo)
    loaded_todo = repo.load_todo('test')
    # assert
    assert (tmp_path / 'test.csv').exists() is True
    assert loaded_todo.title == 'test'
    assert len(loaded_todo.tasks) == 3
    assert loaded_todo.tasks[0].id == tasks[0].id
    assert loaded_todo.tasks[0].description == tasks[0].description
    assert loaded_todo.tasks[0].priority == tasks[0].priority
    assert loaded_todo.tasks[0].status == tasks[0].status
    assert loaded_todo.tasks[0].due == tasks[0].due

def test_load_todo_missing_file(tmp_path: Path) -> None:
    repo = CsvRepository(tmp_path)
    with pytest.raises(FileNotFoundError):
        repo.load_todo('missing')

def test_list_todos(tmp_path: Path) -> None:
    # arange
    repo = CsvRepository(tmp_path)
    repo.save_todo(ToDoList('a'))
    repo.save_todo(ToDoList('b'))
    # act
    result = repo.list_todos()
    # assert
    assert result == {'1': 'a', '2': 'b'}

def test_delete_todo_existing(tmp_path: Path) -> None:
    # arange
    repo = CsvRepository(tmp_path)
    repo.save_todo(ToDoList('test'))
    # act
    result = repo.delete_todo('test')
    # assert
    assert result is True

def test_delete_todo_missing(tmp_path: Path) -> None:
    # arange
    repo = CsvRepository(tmp_path)
    # act
    result = repo.delete_todo('test')
    #assert
    assert result is False