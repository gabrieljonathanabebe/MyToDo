from .base import AppStateBase, AppLike
from clients.cli import ui

class ListOverviewState(AppStateBase):
    def __init__(self):
        self.name = 'LIST OVERVIEW'
        self.options = {
            'b': 'Back',
            '0': 'Exit'
        }

    def _get_options(self, app: AppLike) -> dict[str, str]:
        listed_todo_titles = app.service.repo.list_todo_titles()
        return listed_todo_titles | self.options
        
    def render(self, app: AppLike):
        options = self._get_options(app)
        display_menu = ui.make_menu(
            self.name, self.WIDTH, options=options
        )
        print('\n'.join(display_menu))

    def handle_input(self, app: AppLike, cmd: str):
        if cmd not in self.options.keys():
            app.current_todo = app.service.repo.open_todo_by_choice(cmd)
            if app.current_todo is None:
                app.flash('error', f'To-Do with ID {cmd} not found.')
            else:
                app.goto('list_menu')
        elif cmd == 'b':
            app.goto('main')
        elif cmd == '0':
            app.goto('exit')
        else:
            app.flash('error', 'Unknown command.')