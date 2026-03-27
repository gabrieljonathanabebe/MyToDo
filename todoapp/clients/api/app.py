# todoapp/clients/api/app.py

from fastapi import FastAPI

from todoapp.clients.api.routes import auth, todo_summary, todo_detail


app = FastAPI(title='ToDoScope')


@app.get('/')
def home() -> dict[str, str]:
    return {
        'message': 'Welcome to ToDoScope API',
        'docs': '/docs'
    }


@app.get('/health')
def health() -> dict[str, str]:
    return {'status': 'ok'}


app.include_router(auth.router, prefix='/auth', tags=['auth'])
app.include_router(todo_summary.router, tags=['todo-summary'])
app.include_router(todo_detail.router, tags=['todo-detail'])