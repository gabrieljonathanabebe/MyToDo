# todoapp/clients/cli/states/todo_detail.py

from todoapp.clients.cli import ui, prompts
from .base import AppStateBase, AppLike


class ToDoDetailState(AppStateBase):
    def __init__(self):
        super().__init__()
        self.name = "TODO DETAIL"
        self.options = {
            "a": {"label": "Add Task", "handler": self._cmd_create_task},
            "d": {"label": "Delete Task", "handler": self._cmd_delete_task},
            "s": {"label": "Sort", "handler": self._cmd_sort_tasks},
            "n": {"label": "Assign new IDs", "handler": self._cmd_assign_new_ids},
            "t": {"label": "Toggle status", "handler": self._cmd_toggle_status},
            "b": {"label": "Back", "handler": self._cmd_back},
            "lo": {"label": "Logout", "handler": self._cmd_logout},
            "x": {"label": "Exit", "handler": self._cmd_exit},
        }

    # ===== RENDER ============================================================
    def render(self, app: AppLike):
        display_table = ui.make_table(
            title=app.current_todo.title,
            objects=app.current_todo.tasks,
            spec=ui.TASK_SPEC,
            adapter=ui.task_to_row,
            use_ui_index=False,
        )
        print("\n".join(display_table))
        self._render_options()

    # ===== COMMANDS ==========================================================
    def _cmd_create_task(self, app: AppLike) -> None:
        description_input, priority_input, due_input = prompts.prompt_new_task()
        res = app.service.create_task(
            app.current_todo, description_input, priority_input, due_input
        )
        app.flash("success" if res.ok else "error", res.msg)

    def _cmd_delete_task(self, app: AppLike) -> None:
        task_id_input = prompts.prompt_target_id()
        res = app.service.delete_task(app.current_todo, task_id_input)
        app.flash("success" if res.ok else "error", res.msg)

    def _cmd_sort_tasks(self, app: AppLike) -> None:
        key_input, reverse_input = prompts.prompt_sort_key()
        res = app.service.sort_tasks(app.current_todo, key_input, reverse_input)
        app.flash("success" if res.ok else "error", res.msg)

    def _cmd_assign_new_ids(self, app: AppLike) -> None:
        res = app.service.assign_new_ids(app.current_todo)
        app.flash("success", res.msg)

    def _cmd_toggle_status(self, app: AppLike) -> None:
        task_id_input = prompts.prompt_target_id()
        res = app.service.toggle_status(app.current_todo, task_id_input)
        app.flash("success" if res.ok else "error", res.msg)

    def _cmd_back(self, app: AppLike) -> None:
        app.goto("todo_summary")
