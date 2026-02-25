from .base import AppStateBase, AppLike
from clients.cli import ui
import prompts

class MainMenuState(AppStateBase):
    def __init__(self):
        self.name = 'MAIN MENU'
        self.options = {
            '1': 'New To-Do List',
            '2': 'List Overview',
            '0': 'Exit'
        }

    def render(self, app):
        display_menu = ui.make_menu(self.name, self.WIDTH, options=self.options)
        print('\n'.join(display_menu))

    def handle_input(self, app: AppLike, cmd: str):
        if cmd == '1':
            title = prompts.prompt_todo_title()
            if title in app.service.repo.list_todo_titles().values():
                confirmed = prompts.prompt_open_existing_list(title)
                if confirmed:
                    app.current_todo = app.service.repo.open_todo_by_title(title)
                    app.goto('list_menu')
            else:
                new_todo = app.service.new_todo(title)
                app.flash('success', f'{new_todo.title} successfully created.')
        elif cmd == '2':
            app.goto('overview')
        elif cmd == '0':
            app.goto('exit')
        else:
            app.flash('error', 'Unknown command')