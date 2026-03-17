from typing import Callable

from todoapp.clients.cli import ui, prompts
from .base import AppStateBase, AppLike
from todoapp.core.results import Code


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


    # ===== HELPER===================================================
    def _resolve_choice(self, choice: str) -> str | None:
        try:
            index = int(choice) - 1
        except ValueError:
            return None
        if index < 0 or index >= len(self.todo_items):
            return None
        return self.todo_items[index].id
    
    
    # ===== RENDER-METHODS ==========================================
    def _render_options(self) -> None:
        menu_labels = {cmd: meta['label'] for cmd, meta in self.options.items()}
        ui.info('\n Press a digit to open or:')
        for cmd, label in menu_labels.items():
            ui.info(f'  - {cmd} for {label}')
        ui.info('')
        
    def render(self, app: AppLike):
        res = app.service.list_todos()
        self.todo_items = res.data or []
        display_table = ui.make_table(
            title=self.name,
            objects=self.todo_items,
            spec=ui.TODO_SUMMARY_SPEC,
            adapter=ui.todo_summary_to_row,
            use_ui_index=True
        )
        print('\n'.join(display_table))
        self._render_options()


    # ===== HANDLER-HELPER ==========================================
    def _cmd_new(self, app: AppLike) -> None:
        title = prompts.prompt_todo_title()
        res = app.service.new_todo(title)
        if res.code == Code.ALREADY_EXISTS:
            confirmed = prompts.prompt_open_existing_list(res.msg)
            if confirmed and res.data is not None:
                app.current_todo = res.data
                app.goto('list_menu')
            return
        if not res.ok:
            app.flash('error', res.msg)
        app.flash('success', res.msg)
        app.current_todo = res.data
        app.goto('list_menu')

    def _cmd_delete(self, app: AppLike) -> None:
        choice = prompts.prompt_delete_task()
        todo_id = self._resolve_choice(choice)
        if todo_id is None:
            app.flash('error', 'Invalid selection.')
        res = app.service.delete_todo(todo_id)
        app.flash('success' if res.ok else 'error', res.msg)

    def _cmd_exit(self, app: AppLike) -> None:
        app.goto('exit')


    # ===== HANDLER =================================================
    def handle_input(self, app: AppLike, cmd: str) -> None:
        cmd = cmd.strip().lower()
        if cmd.isdigit():
            todo_id = self._resolve_choice(cmd)
            if todo_id is None:
                app.flash('error', 'Invalid selection.')
                return
            res = app.service.open_todo(todo_id)
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