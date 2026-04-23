# tests/fakes.py

from todoapp.domain.todo_list import ToDoList
from todoapp.domain.models import ToDoSummary


class FakeRepo:
    def __init__(self):
        self.todos_by_id: dict[str, ToDoList] = {}
        self.todo_summaries_by_id: dict[str, ToDoSummary] = {}

    # ===== TODO ==========================================================
    def load_todo(self, todo_id: str) -> ToDoList | None:
        return self.todos_by_id.get(todo_id)

    def save_todo(self, todo: ToDoList) -> None:
        self.todos_by_id[todo.id] = todo

    def delete_todo(self, todo_id: str) -> bool:
        deleted_todo = self.todos_by_id.pop(todo_id, None)
        self.todo_summaries_by_id.pop(todo_id, None)
        return deleted_todo is not None

    # ===== TODO SUMMARY ==================================================
    def register_todo_summary(self, todo: ToDoList) -> None:
        self.todo_summaries_by_id[todo.id] = ToDoSummary.from_todo(todo)

    def update_todo_summary(self, todo: ToDoList) -> None:
        self.todo_summaries_by_id[todo.id] = ToDoSummary.from_todo(todo)

    def get_todo_summary_by_id(self, todo_id: str) -> ToDoSummary | None:
        return self.todo_summaries_by_id.get(todo_id)

    def get_todo_summary_by_title(self, title: str) -> ToDoSummary | None:
        return next(
            (
                summary
                for summary in self.todo_summaries_by_id.values()
                if summary.title == title
            ),
            None,
        )

    def get_todos(self) -> list[ToDoSummary]:
        return sorted(
            self.todo_summaries_by_id.values(),
            key=lambda summary: summary.updated_at,
            reverse=True,
        )