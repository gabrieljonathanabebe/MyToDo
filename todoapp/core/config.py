# todoapp/core/config.py

from __future__ import annotations
import os
from pathlib import Path
from dotenv import load_dotenv


load_dotenv()

DATA_DIR = Path(os.getenv('DATA_DIR', './data')).expanduser().resolve()
USERS_DIR = DATA_DIR / 'users'
USERS_FILE = USERS_DIR / 'users.json'


def get_user_data_dir(username: str) -> Path:
    return USERS_DIR / username