""""
Модуль 16 задание 5
Домашнее задание по теме "Шаблонизатор Jinja 2."
Задача "Список пользователей в шаблоне"
"""""

from fastapi import FastAPI, Path, HTTPException, Request
from typing import Annotated
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
users = []
templates = Jinja2Templates(directory='templates')


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get('/')
def first_welcome(request: Request) -> HTMLResponse:
    return templates.TemplateResponse('users.html', {'request': request, 'users': users})


@app.get('/users/{user_id}')
def welcome(request: Request, user_id: int) -> HTMLResponse:
    return templates.TemplateResponse('users.html', {'request': request, 'user': users[user_id - 1]})


@app.post('/user/{username}/{age}')
async def create_new_user(
        username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
        age: Annotated[int, Path(ge=18, le=120, description='Enter Age', example='24')]) -> User:
    new_id = users[-1].id + 1 if users else 1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example='1')],
                      username: Annotated[
                          str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
                      age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='24')]) -> User:
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User was not found")


@app.delete('/user/{user_id}')
async def del_user(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example='1')]) -> User:
    for index, user in enumerate(users):
        if user.id == user_id:
            return users.pop(index)
    raise HTTPException(status_code=404, detail="User was not found")

# для запуска python -m uvicorn module_16_5:app
