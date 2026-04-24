# mytodo/clients/cli/states/todo_summary.py

from mytodo.clients.cli import ui, prompts
from .base import AppStateBase, AppLike
from mytodo.core.results import Code


class ToDoSummaryState(AppStateBase):
    def __init__(self):
        super().__init__()
        self.name = "TODO SUMMARIES"
        self.options = {
            "n": {
                "label": "New To-Do",
                "handler": self._cmd_new,
            },
            "d": {"label": "Delete To-Do", "handler": self._cmd_delete},
            "lo": {"label": "Logout", "handler": self._cmd_logout},
            "x": {"label": "Exit", "handler": self._cmd_exit},
        }

    # ===== HELPER ============================================================
    def _resolve_choice(self, choice: str) -> str | None:
        try:
            index = int(choice) - 1
        except ValueError:
            return None
        if index < 0 or index >= len(self.todo_items):
            return None
        return self.todo_items[index].id

    # ===== RENDER ============================================================
    def render(self, app: AppLike):
        res = app.service.get_todos()
        self.todo_items = res.data or []
        display_table = ui.make_table(
            title=self.name,
            objects=self.todo_items,
            spec=ui.TODO_SUMMARY_SPEC,
            adapter=ui.todo_summary_to_row,
            use_ui_index=True,
        )
        print("\n".join(display_table))
        self._render_options(intro="\n Press a digit to open or:")

    # ===== COMMANDS ==========================================================
    def _cmd_new(self, app: AppLike) -> None:
        title = prompts.prompt_todo_title()
        res = app.service.create_todo(title)
        if res.code == Code.ALREADY_EXISTS:
            confirmed = prompts.prompt_open_existing_list(res.msg)
            if confirmed and res.data is not None:
                app.current_todo = res.data
                app.goto("todo_summary")
            return
        if not res.ok:
            app.flash("error", res.msg)
            return
        app.flash("success", res.msg)
        app.current_todo = res.data
        app.goto("todo_summary")

    def _cmd_delete(self, app: AppLike) -> None:
        choice = prompts.prompt_delete_task()
        todo_id = self._resolve_choice(choice)
        if todo_id is None:
            app.flash("error", "Invalid selection.")
            return
        res = app.service.delete_todo(todo_id)
        app.flash("success" if res.ok else "error", res.msg)

    # ===== INPUT =============================================================
    def handle_input(self, app: AppLike, cmd: str) -> None:
        cmd = cmd.strip().lower()
        if cmd.isdigit():
            todo_id = self._resolve_choice(cmd)
            if todo_id is None:
                app.flash("error", "Invalid selection.")
                return
            res = app.service.open_todo(todo_id)
            if not res.ok:
                app.flash("error", res.msg)
                return
            app.current_todo = res.data
            app.goto("todo_detail")
            return
        super().handle_input(app, cmd)
