import todoapp.core.config as cfg
from todoapp.core.service import ToDoService
from todoapp.infra.csv_repository import CsvRepository


def get_service() -> ToDoService:
    repo = CsvRepository(cfg.DATA_DIR)
    return ToDoService(repo)