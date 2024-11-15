from fastapi import APIRouter, Depends, status, HTTPException
from slugify import slugify
from sqlalchemy.orm import Session
from app.backend.db_depends import get_db
from typing import Annotated
from app.models import Task, User
from app.schemas import CreateTask, UpdateTask
from sqlalchemy import insert, select, update, delete

router = APIRouter(prefix='/task', tags=['task'])


@router.get('/')
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    task_all = db.scalars(select(Task)).all()
    return task_all


@router.get('/task_id')
async def task_by_id(db: Annotated[Session, Depends(get_db)], task_id: int):
    task_find = db.scalar(select(Task).where(Task.id == task_id))
    if task_find is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Task was not found')
    else:
        return task_find


@router.post('/create')
async def create_task(db: Annotated[Session, Depends(get_db)], task_create: CreateTask, user_id: int):
    user_find = db.scalar(select(User).where(User.id == user_id))
    if user_find is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User was not found')
    else:
        db.execute(insert(Task).values(title=task_create.title,
                                       content=task_create.content,
                                       priority=task_create.priority,
                                       user_id=user_id,
                                       slug=slugify(task_create.title)))
        db.commit()
        return {
            'status_code': status.HTTP_201_CREATED,
            'transaction': 'Successful'}


@router.put('/update')
async def update_task(db: Annotated[Session, Depends(get_db)], task_update: UpdateTask, user_id: int):
    user_find = db.scalar(select(User).where(User.id == user_id))
    if user_find is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User was not found"')
    else:
        db.execute(update(Task).where(Task.user_id == user_id).values(title=task_update.title,
                                                                      content=task_update.content,
                                                                      priority=task_update.priority))
        db.commit()
        return {
            'status_code': status.HTTP_200_OK,
            'transaction': 'User update is Successful!'}


@router.delete('/delete')
async def delete_task(db: Annotated[Session, Depends(get_db)], task_id: int):
    task_find = db.scalar(select(Task).where(Task.id == task_id))
    if task_find is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User was not found"')
    else:
        db.execute(delete(Task).where(Task.id == task_id))
        db.commit()
        return {
            'status_code': status.HTTP_200_OK,
            'transaction': 'Task delete is Successful!'}
