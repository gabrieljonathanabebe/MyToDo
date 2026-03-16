from typing import Callable

from todoapp.clients.cli import ui, prompts
from .base import AppStateBase, AppLike


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
            't': {
                'label': 'Toggle status',
                'handler': self._cmd_toggle_status
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
            objects=app.current_todo.tasks,
            spec=ui.TASK_SPEC,
            adapter=ui.task_to_row,
            use_ui_index=False
        )
        print('\n'.join(display_table))
        self._render_options()


    # ===== HANDLER-HELPER ==========================================
    def _cmd_add_task(self, app: AppLike) -> None:
        description_input, priority_input, due_input = prompts.prompt_new_task()
        res = app.service.add_task(
            app.current_todo, description_input, priority_input, due_input
        )
        app.flash('success' if res.ok else 'error', res.msg)

    def _cmd_delete_task(self, app: AppLike) -> None:
        task_id_input = prompts.prompt_target_id()
        res = app.service.delete_task(app.current_todo, task_id_input)
        app.flash('success' if res.ok else 'error', res.msg)

    def _cmd_sort_todo(self, app: AppLike) -> None:
        key_input, reverse_input = prompts.prompt_sort_key()
        res = app.service.sort_todo(app.current_todo, key_input, reverse_input)
        app.flash('success' if res.ok else 'error', res.msg)

    def _cmd_assign_new_ids(self, app: AppLike) -> None:
        res = app.service.assign_new_ids(app.current_todo)
        app.flash('success', res.msg)

    def _cmd_toggle_status(self, app: AppLike) -> None:
        task_id_input = prompts.prompt_target_id()
        res = app.service.toggle_status(app.current_todo, task_id_input)
        app.flash('success' if res.ok else 'error', res.msg)

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