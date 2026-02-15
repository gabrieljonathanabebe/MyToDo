import os
from pathlib import Path
import time

from todo_list import ToDoList
from states import MainMenuState


class ToDoApp:
    def __init__(self):
        self.running = True
        self.state = MainMenuState()
        self.DATA_DIR = Path.cwd() / 'data'
        self.todo_list = None

    def set_state(self, new_state):
        self.state = new_state

    def create_new_list(self):
        title = input('Select a title for your new To-Do List: ')
        todo_list = ToDoList(title)

    def list_saved_csvs(self) -> dict[int, str]:
        all_lists = [
            l.stem for l in self.DATA_DIR.iterdir() if l.suffix == '.csv'
        ]
        idx = list(range(1, len(all_lists) + 1))
        all_lists = dict(zip(idx, all_lists))
        return all_lists
    
    def open_list(self, cmd: str):
        all_lists = self.list_saved_csvs()
        selected_idx = int(cmd)
        title = all_lists.get(selected_idx)
        self.todo_list = ToDoList.load_todo(title, self.DATA_DIR)
    
    def save_list(self) -> None:
        return self.todo_list.save_todo(self.DATA_DIR)
    
    def clear_display(self) -> None:
        time.sleep(0.1)
        os.system('cls' if os.name == 'nt' else 'clear')

    def run(self):
        while self.running:
            self.clear_display()
            self.state.render(self)
            if not self.running:
                break
            cmd = input(f'> {self.state.question}').strip()
            self.state.handle_input(self, cmd)
            

def main() -> None:
    app = ToDoApp()
    app.run()


if __name__ == '__main__':
    main()