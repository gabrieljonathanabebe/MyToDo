# todoapp/core/services/messages.py


class ToDoMessage:
    @staticmethod
    def todo_not_found() -> str:
        return 'To-Do not found.'
    
    @staticmethod
    def task_not_found(task_id: str) -> str:
        return f'Task {task_id} not found.'
    
    @staticmethod
    def task_updated(task_id: str) -> str:
        return f'Task {task_id} updated.'

    @staticmethod
    def invalid_task_id(task_id: str) -> str:
        return f'"{task_id}" is not a valid task id.'
    
    @staticmethod
    def task_added(task_id: str) -> str:
        return f'Task {task_id} deleted.' 

    @staticmethod
    def task_deleted(task_id: str) -> str:
        return f'Task {task_id} deleted.'

    @staticmethod
    def todo_created(title: str) -> str:
        return f'{title} created.'

    @staticmethod
    def todo_deleted(title: str) -> str:
        return f'To-Do "{title}" deleted.'
    
    @staticmethod
    def task_status_toggled(task_id: str) -> str:
        return f'Toggle status for Task {task_id}.'
    
    @staticmethod
    def invalid_status(status: str) -> str:
        return f'"{status}" is not a valid status'

    @staticmethod
    def task_status_updated(task_id: str, status: str) -> str:
        return f'Task {task_id} status updated to "{status}".'

    @staticmethod
    def task_created(task_id: int) -> str:
        return f'Task {task_id} added.'

    @staticmethod
    def todo_already_exists(title: str) -> str:
        return f'{title} already exists.'

    @staticmethod
    def todo_not_found() -> str:
        return 'To-Do not found.'