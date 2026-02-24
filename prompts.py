

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