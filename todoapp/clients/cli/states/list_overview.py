from typing import Callable

from todoapp.clients.cli import ui, prompts
from .base import AppStateBase, AppLike


class ListOverviewState(AppStateBase):
    def __init__(self):
        self.name = 'LIST OVERVIEW'
        self.options = {
            'n': {
                'label': 'New To-Do',
                'handler': self._cmd_new,
            },
            'd': {
                'label': 'Delete To-Do',
                'handler': self._cmd_delete
            },
            'x': {
                'label': 'Exit',
                'handler': self._cmd_exit
            }
        }
    
    
    # ===== RENDER-METHODS ==========================================
    def _render_options(self) -> None:
        menu_labels = {cmd: meta['label'] for cmd, meta in self.options.items()}
        ui.info('\n Press a digit to open or:')
        for cmd, label in menu_labels.items():
            ui.info(f'  - {cmd} for {label}')
        ui.info('')
        
    def render(self, app: AppLike):
        res = app.service.list_todos()
        self.todos = res.data
        display_menu = ui.make_menu(
            self.name, self.WIDTH, data=self.todos
        )
        print('\n'.join(display_menu))
        self._render_options()


    # ===== HANDLER-HELPER ==========================================
    def _cmd_new(self, app: AppLike) -> None:
        title = prompts.prompt_todo_title()
        res = app.service.new_todo(title)
        if not res.ok:
            confirmed = prompts.prompt_open_existing_list(res.msg)
            if confirmed:
                res = app.service.open_todo_by_title(title)
                app.current_todo = res.data
                app.goto('list_menu')
            return
        app.flash('success', res.msg)
        app.current_todo = res.data
        app.goto('list_menu')

    def _cmd_delete(self, app: AppLike) -> None:
        choice = prompts.prompt_delete_task()
        res = app.service.delete_todo_by_choice(choice)
        app.flash('success' if res.ok else 'error', res.msg)

    def _cmd_exit(self, app: AppLike) -> None:
        app.goto('exit')


    # ===== HANDLER =================================================
    def handle_input(self, app: AppLike, cmd: str) -> None:
        cmd = cmd.strip().lower()
        if cmd.isdigit():
            res = app.service.open_todo_by_choice(cmd)
            if not res.ok:
                app.flash('error', res.msg)
                return
            app.current_todo = res.data
            app.goto('list_menu')
            return
        entry = self.options.get(cmd)
        if not entry:
            app.flash('error', 'Unknown command.')
            return
        handler: Callable[[AppLike], None] = entry['handler']
        handler(app)