import os
from pathlib import Path
import time

from service import ToDoService
from domain import ToDoList
from repository import CsvRepository
from clients.cli.states import router
from clients.cli import ui

class ToDoApp:
    def __init__(self):
        self.DATA_DIR = Path.cwd() / 'data'
        repo = CsvRepository(self.DATA_DIR)
        self.service = ToDoService(repo)
        self.running = True
        self.goto('overview')
        self.flash_msg = None
        self.current_todo = None

    def goto(self, state_name: str) -> None:
        self.state = router.set_state(state_name)

    def flash(self, kind: str, msg: str) -> None:
        self.flash_msg = (kind, msg)

    def new_list(self):
        title = input('Select a title for your new To-Do List: ')
        todo_list = ToDoList(title)
        pass # <-- will be completed
    
    def clear_display(self) -> None:
        time.sleep(0.1)
        os.system('cls' if os.name == 'nt' else 'clear')

    def run(self):
        while self.running:
            self.clear_display()
            self.state.render(self)
            if self.flash_msg:
                kind, msg = self.flash_msg
                if kind == 'success':
                    ui.success(msg + '\n')
                elif kind == 'info':
                    ui.info(msg + '\n')
                elif kind == 'warning':
                    ui.warning(msg + '\n')
                else:
                    ui.error(msg + '\n')
                self.flash_msg = None
            if not self.running:
                break
            cmd = input(f'> ').strip()
            self.state.handle_input(self, cmd)
            

def main() -> None:
    app = ToDoApp()
    app.run()


if __name__ == '__main__':
    main()