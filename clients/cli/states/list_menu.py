from pydantic import ValidationError

from .base import AppStateBase, AppLike
from clients.cli import ui
import prompts


class ListMenuState(AppStateBase):
    def __init__(self):
        self.name = 'LIST MENU'
        self.options = {
            '1': 'Add Task',
            '2': 'Delete Task',
            '3': 'Save',
            '4': 'Sort',
            '5': 'Assign new IDs',
            'b': 'Back',
            '0': 'Exit'
        }
    
    def render(self, app: AppLike):
        display_table = ui.make_table(
            title=app.current_todo.title,
            tasks=app.current_todo.tasks
        )
        display_menu = ui.make_menu(self.name, self.WIDTH, options=self.options)
        print('\n'.join(display_table))
        print('\n'.join(display_menu))


    def handle_input(self, app: AppLike, cmd):
        if cmd == '1':
            try:
                task, priority, due = prompts.prompt_new_task()
                new_task = app.service.add_task(
                    app.current_todo, task, priority, due
                )
                app.flash('success', f'Task {new_task.id} added.')
            except ValidationError as e:
                app.flash('error', 'Error during validation.')    
        elif cmd == '2':
            try:
                target_id = prompts.prompt_target_id()
                ok = app.service.delete_task(app.current_todo, int(target_id))
                app.flash('success', f'Task {target_id} deleted.')
            except ValueError:
                app.flash('error', f'Please enter a number.')
        elif cmd == '3':
            app.service.repo.save_todo(app.current_todo)
        elif cmd == '4':
            app.service.sort_todo(app.current_todo)
        elif cmd == '5':
            app.service.assign_new_ids(app.current_todo)
        elif cmd == 'b':
            app.goto('overview')
        elif cmd == '0':
            app.goto('exit')
        else:
            app.flash('error', 'Unknown command')