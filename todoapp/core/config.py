# todoapp/core/config.py

from __future__ import annotations
import os
from pathlib import Path
from dotenv import load_dotenv


load_dotenv()


# ===== CONSTANTS =============================================================
DATA_DIR = Path(os.getenv('DATA_DIR', './data')).expanduser().resolve()
USERS_DIR = DATA_DIR / 'users'
USERS_FILE = USERS_DIR / 'users.json'

FRONTEND_ORIGINS = [
    origin.strip()
    for origin in os.getenv(
        'FRONTEND_ORIGINS',
        'http://localhost:5173,http://127.0.0.1:5173'
    ).split(',')
]


# ===== FUNCTIONS =============================================================
def get_user_data_dir(username: str) -> Path:
    return USERS_DIR / username