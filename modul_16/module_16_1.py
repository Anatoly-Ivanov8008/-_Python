""""
Модуль 16 задание 1
Домашнее задание по теме "Основы Fast Api и маршрутизация"
Задача "Начало пути"
"""""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def welcome() -> dict:
    return {"message": "Главная страница"}


@app.get("/user/admin")
async def welcome_admin() -> dict:
    return {"message": "Вы вошли как администратор"}


@app.get("/user/{user_id}")
async def users_id(user_id: str) -> dict:
    return {"message": f"Вы вошли как пользователь № {user_id}"}


@app.get("/user")
async def welcome_users_id(username: str = 'неизвестный пользователь', age: int = 0) -> dict:
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}
