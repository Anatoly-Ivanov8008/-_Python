from fastapi import FastAPI
from routers import user
from routers import task

app = FastAPI()


@app.get('/')
async def welcome():
    return {"message": "Welcome to Taskmanager"}


app.include_router(user.router)
app.include_router(task.router)

# для запуска необходимо быть в каталоге с файлом main и набрать:
# python -m uvicorn main:app

# для перехода в другой каталог
# cd ...
