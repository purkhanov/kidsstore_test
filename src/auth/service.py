from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from src.users.schemas import UserCreateSchema
from src.users.service import UserService


oauth2_bearer = OAuth2PasswordBearer(tokenUrl="/auth/token")


async def authenticate_user():
    pass


async def create_user(data: UserCreateSchema, db_session: AsyncSession):
    await UserService(db_session).create_user(data)

