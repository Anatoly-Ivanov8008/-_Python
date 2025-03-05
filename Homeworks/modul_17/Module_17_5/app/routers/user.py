from fastapi import APIRouter, Depends, status, HTTPException
from slugify import slugify
from sqlalchemy.orm import Session
from app.backend.db_depends import get_db
from typing import Annotated
from app.models import User, Task
from app.schemas import CreateUser, UpdateUser
from sqlalchemy import insert, select, update, delete

router = APIRouter(prefix='/user', tags=['user'])


@router.get('/')
async def all_users(db: Annotated[Session, Depends(get_db)]):
    users_all = db.scalars(select(User)).all()
    return users_all


@router.get('/user_id')
async def user_by_id(db: Annotated[Session, Depends(get_db)], user_id: int):
    user_find = db.scalar(select(User).where(User.id == user_id))
    if user_find is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User was not found')
    else:
        return user_find


@router.post('/create')
async def create_user(db: Annotated[Session, Depends(get_db)], user_create: CreateUser):
    user_find = db.scalar(select(User).where(User.username == user_create.username))
    if user_find is not None:
        raise HTTPException(
            status_code=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION,
            detail='Пользователь уже существует')
    else:
        db.execute(insert(User).values(username=user_create.username,
                                       firstname=user_create.firstname,
                                       lastname=user_create.lastname,
                                       age=user_create.age,
                                       slug=slugify(user_create.username)))
        db.commit()
        return {
            'status_code': status.HTTP_201_CREATED,
            'transaction': 'Successful'}


@router.put('/update')
async def update_user(db: Annotated[Session, Depends(get_db)], user_update: UpdateUser, user_id: int):
    user_find = db.scalar(select(User).where(User.id == user_id))
    if user_find is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User was not found"')
    else:
        db.execute(update(User).where(User.id == user_id).values(firstname=user_update.firstname,
                                                                 lastname=user_update.lastname,
                                                                 age=user_update.age))
        db.commit()
        return {
            'status_code': status.HTTP_200_OK,
            'transaction': 'User update is Successful!'}


@router.delete('/delete')
async def delete_user(db: Annotated[Session, Depends(get_db)], user_id: int):
    user_find = db.scalar(select(User).where(User.id == user_id))
    if user_find is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User was not found"')
    else:
        db.execute(delete(User).where(User.id == user_id))
        db.execute(delete(Task).where(Task.user_id == user_id))
        db.commit()
        return {
            'status_code': status.HTTP_200_OK,
            'transaction': 'User and Task delete is Successful!'}


@router.get('/user_id/tasks')
async def tasks_by_user_id(db: Annotated[Session, Depends(get_db)], user_id: int):
    tasks_find = db.scalar(select(Task).where(Task.user_id == user_id))
    if tasks_find is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User was not found')
    else:
        return tasks_find
