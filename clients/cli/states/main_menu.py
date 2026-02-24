from .base import AppStateBase, AppLike
from clients.cli import ui

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
            app.new_list()
        elif cmd == '2':
            app.goto('overview')
        elif cmd == '0':
            app.goto('exit')
        else:
            app.flash('error', 'Unknown command')