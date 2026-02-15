from pathlib import Path

ROOT_DIR = Path.cwd()
DATA_DIR = ROOT_DIR / 'data'

def get_path(title: str) -> Path:
    return DATA_DIR / f'{title}.csv'