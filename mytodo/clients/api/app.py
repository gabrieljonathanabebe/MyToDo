# mytodo/clients/api/app.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from mytodo.clients.api.routes import auth, todo_summary, todo_detail
import mytodo.core.config as cfg


app = FastAPI(title="MyToDo")

app.add_middleware(
    CORSMiddleware,
    allow_origins=cfg.FRONTEND_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home() -> dict[str, str]:
    return {"message": "Welcome to MyToDo API", "docs": "/docs"}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(
    todo_summary.router, prefix="/users/{username}/todos", tags=["todo-summary"]
)
app.include_router(
    todo_detail.router, prefix="/users/{username}/todos/{todo_id}", tags=["todo-detail"]
)
