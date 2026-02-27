from __future__ import annotations
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

DATA_DIR = Path(os.getenv('DATA_DIR', './data')).expanduser().resolve()