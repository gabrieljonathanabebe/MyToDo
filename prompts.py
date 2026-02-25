

def _validate_input(raw_input: str) -> str:
    return input(f'{raw_input} ').strip()

def prompt_new_task() -> tuple[str, str, str | None]:
    task = _validate_input('Task:')
    priority = _validate_input('Priority (1-3):')
    due_raw = _validate_input('Due (YYYY-MM-DD) or empty:')
    due = due_raw or None
    return task, priority, due

def prompt_target_id() -> str:
    return _validate_input('Select target id:')

def prompt_sort_key() -> tuple[str, bool]:
    key = _validate_input('Sort key:').lower().replace(' ', '_')
    order = _validate_input('Sorting reverse (y/n)?')
    reverse = True if order == 'y' else False
    return key, reverse


def prompt_todo_title() -> str:
    return _validate_input('Select title for new ToDo:')

def prompt_open_existing_list(title: str) -> bool:
    confirmed = _validate_input(f'{title} already exists. Open(y/n)?')
    return (confirmed == 'y')
