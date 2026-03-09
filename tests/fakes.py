from todoapp.domain.todo_list import ToDoList


class FakeRepo:
    def __init__(self):
        self.todos: dict[str, ToDoList] = {}

    def load_todo(self, title: str) -> ToDoList | None:
        return self.todos.get(title)

    def save_todo(self, todo: ToDoList) -> None:
        self.todos[todo.title] = todo

    def delete_todo(self, title: str) -> bool:
        deleted = self.todos.pop(title, None)
        if deleted is None:
            return False
        return True

    def list_todos(self) -> dict[str, str]:
        todo_titles = sorted(list(self.todos.keys()))
        return {str(i + 1): title for i, title in enumerate(todo_titles)}