import os
import time

import todoapp.core.factories as factories
from todoapp.clients.cli.states import router
from todoapp.clients.cli import ui


class ToDoApp:
    def __init__(self):
        self.user_service = factories.build_user_service()
        self.service = None
        self.current_user = None
        self.running = True
        self.goto('login')
        self.flash_msg = None
        self.current_todo = None

    def goto(self, state_name: str) -> None:
        self.state = router.set_state(state_name)

    def flash(self, kind: str, msg: str) -> None:
        self.flash_msg = (kind, msg)
    
    def clear_display(self) -> None:
        time.sleep(0.1)
        os.system('cls' if os.name == 'nt' else 'clear')

    def run(self):
        while self.running:
            self.clear_display()
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
            self.state.render(self)
            if not self.running:
                break
            cmd = input(f'> ').strip()
            self.state.handle_input(self, cmd)
            

def main() -> None:
    app = ToDoApp()
    app.run()


if __name__ == '__main__':
    main()