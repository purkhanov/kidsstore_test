from typing import Annotated
from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from src.dependencies import db_dependency
from src.users.schemas import UserCreateSchema
from src.auth.schemas import TokenResponseSchema
from src.auth.service import create_user
from src.database.exceptions import AlreadyExists


router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/sign-up", status_code=status.HTTP_201_CREATED)
async def sign_up(user_request: UserCreateSchema, db: db_dependency):
    await create_user(user_request, db)


@router.post(
    "/token", status_code=status.HTTP_200_OK, response_model=TokenResponseSchema
)
async def sign_in(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dependency
):
    pass
