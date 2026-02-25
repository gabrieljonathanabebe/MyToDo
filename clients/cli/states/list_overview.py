from .base import AppStateBase, AppLike
from clients.cli import ui
import prompts

class ListOverviewState(AppStateBase):
    def __init__(self):
        self.name = 'LIST OVERVIEW'
        self.options = {
            'n': 'New To-Do',
            'x': 'Exit'
        }
    
    def _render_options(self) -> None:
        ui.info('\n Press a digit to open or:')
        for cmd, label in self.options.items():
            ui.info(f'  - {cmd} for {label}')
        ui.info('')
        
    def render(self, app: AppLike):
        self.listed_todo_titles = app.service.repo.list_todo_titles()
        display_menu = ui.make_menu(
            self.name, self.WIDTH, data=self.listed_todo_titles
        )
        print('\n'.join(display_menu))
        self._render_options()

    def handle_input(self, app: AppLike, cmd: str):
        if cmd == 'n':
            title = prompts.prompt_todo_title()
            if title in self.listed_todo_titles.values():
                confirmed = prompts.prompt_open_existing_list(title)
                if confirmed:
                    app.current_todo = app.service.repo.open_todo_by_title(title)
                    app.goto('list_menu')
            else:
                new_todo = app.service.new_todo(title)
                app.flash('success', f'{new_todo.title} successfully created.')
        elif cmd == 'x':
            app.goto('exit')
        elif cmd.isdigit():
            todo = app.service.repo.open_todo_by_choice(cmd)
            if todo:
                app.current_todo = todo
                app.goto('list_menu')
            else:
                app.flash('error', 'Invalid selection.')
        else:
            app.flash('error', 'Unknown command.')