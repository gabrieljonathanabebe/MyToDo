from typing import Protocol
from todo_list import ToDoList
import ui

class AppLike(Protocol):
    running: bool
    todo_list: ToDoList

    def set_state(self, new_state) -> None:
        ...

    def list_saved_csvs(self) -> dict[int, str]:
        ...

    def create_new_list(self):
        ...

    def open_list(self, cmd: str) -> None:
        ...

    def save_list(self) -> None:
        ...


class AppStateBase:
    name = ''
    WIDTH = 30
    question = ''
    content = None
    cmds = None

    def render(self, app) -> None:
        menu = ui.make_menu(self.name, self.cmds, self.WIDTH)
        print('\n'.join(menu))


    """def render(self, app):
        self._render_border()
        self._render_title()
        if self.content is not None:
            self._render_body()
        if self.cmds is not None:
            self._render_commands()
    
    def _render_border(self, color = None):
        border = '+' + '-' * self.WIDTH + '+'
        if color is not None:
            print(f'{color}{border}')
        else:
            print(border)

    def _render_title(self):
        title = self.name.center(self.WIDTH)
        print(f'|{title}|')

    def _render_body(self):
        self._render_border()
        for idx, item in self.content.items():
            line = f' {idx} → {item.capitalize()}'.ljust(self.WIDTH - 1)
            print(f'| {line}|')
        self._render_border()

    def _render_commands(self):
        self._render_border()
        print('| ' + 'Options:'.ljust(self.WIDTH - 1) + '|')
        for id, cmd in self.cmds.items():
            line = f' {id} → {cmd}'.ljust(self.WIDTH - 1)
            print(f'| {line}|')
        self._render_border()"""
    
    def handle_input(self, app, cmd: str):
        raise NotImplementedError
    

class MainMenuState(AppStateBase):
    def __init__(self):
        self.name = 'MAIN MENU'
        self.cmds = {
            '1': 'New To-Do List',
            '2': 'List Overview',
            '0': 'Exit'
        }


    def handle_input(self, app: AppLike, cmd: str):
        if cmd == '1':
            app.create_new_list()
        elif cmd == '2':
            app.set_state(ListOverviewState())
        elif cmd == '0':
            app.set_state(ExitState())
        else:
            print('Unknown command')


class ListOverviewState(AppStateBase):
    def __init__(self):
        self.name = 'LIST OVERVIEW'
        self.cmds = {
            '1': 'Open List',
            '2': 'Delete List',
            'b': 'Back',
            '0': 'Exit'
        }

    def handle_input(self, app: AppLike, cmd: str):
        if cmd == '1':
            app.set_state(ListDetailsState(app, 'open'))
        elif cmd == '2':
            app.set_state(ListDetailsState(app, 'delete'))
        elif cmd == 'b':
            app.set_state(MainMenuState())
        elif cmd == '0':
            app.set_state(ExitState())
        else:
            print('Unknown command')


class ListDetailsState(AppStateBase):
    def __init__(self, app: AppLike, mode: str):
        self.name = 'LIST DETAILS'
        self.content = self.get_lists(app)
        self.question = f'Which list would you like to {mode}? '

    def get_lists(self, app: AppLike) -> dict[int, str]:
        return app.list_saved_csvs()
    
    def handle_input(self, app: AppLike, cmd: str):
        if int(cmd) in self.content.keys():
            app.set_state(ListMenuState(app, cmd))
        else:
            print('Unknown command')
    

class ListMenuState(AppStateBase):
    def __init__(self, app: AppLike, cmd: str):
        self.name = 'LIST MENU'
        self.cmds = {
            '1': 'Add Task',
            '2': 'Delete Task',
            '3': 'Save',
            '4': 'Sort',
            '5': 'Assign new IDs',
            'b': 'Back',
            '0': 'Exit'
        }
        app.open_list(cmd)
    
    def render(self, app: AppLike):
        app.todo_list.render_table()
        self._render_commands()

    def handle_input(self, app: AppLike, cmd):
        if cmd == '1':
            app.todo_list.add_task()
        elif cmd == '2':
            app.todo_list.delete_task()
        elif cmd == '3':
            app.save_list()
        elif cmd == '4':
            app.todo_list.sort_todo()
        elif cmd == '5':
            app.todo_list.assign_new_ids()
        elif cmd == 'b':
            app.set_state(ListDetailsState(app, 'open'))
        elif cmd == '0':
            app.set_state(ExitState())
        else:
            print('Unknown command.')


class ExitState(AppStateBase):
    def render(self, app: AppLike):
        print('Goodbye 👋')
        app.running = False

    def handle_input(self, app, cmd: str):
        pass