from fastapi import APIRouter, status
from src.dependencies import db_dependency
from src.users.schemas import UserCreateSchema, UserUpdateSchema
from src.users.service import UserService


router = APIRouter(prefix='/users', tags=['users'])


@router.get('', status_code=status.HTTP_200_OK)
async def get_user(user: object, db: db_dependency):
    await UserService(db).get_user(user.id)


@router.post('', status_code=status.HTTP_201_CREATED)
async def create_user(data: UserCreateSchema, db: db_dependency):
    await UserService(db).create_user(data)


@router.put('', status_code=status.HTTP_202_ACCEPTED)
async def update_user(user: object, data: UserUpdateSchema, db: db_dependency):
    await UserService(db).update_user(user.id, data)


@router.delete('', status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user: object, db: db_dependency):
    await UserService(db).delete_user(user.id)
