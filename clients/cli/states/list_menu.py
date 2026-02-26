from typing import Callable

from pydantic import ValidationError

from .base import AppStateBase, AppLike
from clients.cli import ui
import prompts


class ListMenuState(AppStateBase):
    def __init__(self):
        self.name = 'LIST MENU'
        self.options = {
            'a': {
                'label': 'Add Task',
                'handler': self._cmd_add_task
            },
            'd': {
                'label': 'Delete Task',
                'handler': self._cmd_delete_task
            },
            's': {
                'label': 'Sort',
                'handler': self._cmd_sort_todo
            },
            'n': {
                'label': 'Assign new IDs',
                'handler': self._cmd_assign_new_ids
            },
            'b': {
                'label': 'Back',
                'handler': self._cmd_back
            },
            'x': {
                'label': 'Exit',
                'handler': self._cmd_exit
            },
        }


    # ===== RENDER-METHODS ==========================================
    def _render_options(self) -> None:
        menu_labels = {cmd: meta['label'] for cmd, meta in self.options.items()}
        ui.info('\n Press:')
        for cmd, label in menu_labels.items():
            ui.info(f'  - {cmd} for {label}')
        ui.info('')
    
    def render(self, app: AppLike):
        display_table = ui.make_table(
            title=app.current_todo.title,
            tasks=app.current_todo.tasks
        )
        print('\n'.join(display_table))
        self._render_options()


    # ===== HANDLER-HELPER ==========================================
    def _cmd_add_task(self, app: AppLike) -> None:
        try:
            task_input, priority_input, due_input = prompts.prompt_new_task()
            new_task = app.service.add_task(
                app.current_todo, task_input, priority_input, due_input
            )
            app.flash('success', f'Task {new_task.id} added.')
        except ValidationError:
            app.flash('error', f'Error during validation.')

    def _cmd_delete_task(self, app: AppLike) -> None:
        try:
            task_id_input = prompts.prompt_target_id()
            ok = app.service.delete_task(app.current_todo, int(task_id_input))
            if not ok:
                app.flash('error', f'ID {task_id_input} not found.')
                return
            app.flash('success', f'Task {task_id_input} deleted.')
        except ValueError:
            app.flash('error', 'Please enter a number.')

    def _cmd_sort_todo(self, app: AppLike) -> None:
        key_input, reverse_input = prompts.prompt_sort_key()
        res = app.service.sort_todo(app.current_todo, key_input, reverse_input)
        level = 'success' if res.ok else 'error'
        app.flash(level, res.msg)

    def _cmd_assign_new_ids(self, app: AppLike) -> None:
        count = app.service.assign_new_ids(app.current_todo)
        app.flash('success', f'Reassigned {count} IDs.')

    def _cmd_back(self, app: AppLike) -> None:
        app.goto('overview')

    def _cmd_exit(self, app: AppLike) -> None:
        app.goto('exit')


    # ===== HANDLER =================================================
    def handle_input(self, app: AppLike, cmd: str):
        cmd = cmd.strip().lower()
        entry = self.options.get(cmd)
        if not entry:
            app.flash('error', 'Unknown command')
            return
        handler: Callable[[AppLike], None] = entry['handler']
        handler(app)