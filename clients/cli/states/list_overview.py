from typing import Callable

from .base import AppStateBase, AppLike
from clients.cli import ui
import prompts

class ListOverviewState(AppStateBase):
    def __init__(self):
        self.name = 'LIST OVERVIEW'
        self.options = {
            'n': {
                'label': 'New To-Do',
                'handler': self._cmd_new,
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
        self.listed_todo_titles = app.service.repo.list_todo_titles()
        display_menu = ui.make_menu(
            self.name, self.WIDTH, data=self.listed_todo_titles
        )
        print('\n'.join(display_menu))
        self._render_options()


    # ===== HANDLER-HELPER ==========================================
    def _cmd_new(self, app: AppLike) -> None:
        title = prompts.prompt_todo_title()
        if title in self.listed_todo_titles.values():
            confirmed = prompts.prompt_open_existing_list(title)
            if confirmed:
                app.current_todo = app.service.repo.open_todo_by_title(title)
                app.goto('list_menu')
            return
        new_todo = app.service.new_todo(title)
        app.flash('success', f'{new_todo.title} created.')

    def _cmd_exit(self, app: AppLike) -> None:
        app.goto('exit')


    # ===== HANDLER =================================================
    def handle_input(self, app: AppLike, cmd: str) -> None:
        cmd = cmd.strip().lower()
        if cmd.isdigit():
            todo = app.service.repo.open_todo_by_choice(cmd)
            if todo:
                app.current_todo = todo
                app.goto('list_menu')
            else:
                app.flash('error', 'Invalid section')
            return
        entry = self.options.get(cmd)
        if not entry:
            app.flash('error', 'Unknown command.')
            return
        handler: Callable[[AppLike], None] = entry['handler']
        handler(app)
            