from typing import Annotated
from datetime import timedelta, datetime
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from jose import jwt, JWTError
from pydantic import EmailStr
from src.users.schemas import UserCreateSchema, bcrypt_context
from src.users.repository import UserRepository
from src.database.models import User
from src.auth.schemas import TokenResponseSchema, UserAuthSchema
from src.config import settings


oauth2_bearer = OAuth2PasswordBearer(tokenUrl = "/auth/token")


async def authenticate_user(email: EmailStr, passw: str, db_session: AsyncSession) -> User | None:
    user = await UserRepository(db_session).get_user_by_email(email)

    if not user or not bcrypt_context.verify(passw, user.password):
        return False
    
    return user


def cteate_access_token(user: User, expires: timedelta) -> str:
    expires = datetime.now() + expires
    encode = {
        "id": user.id,
        "exp": expires,
    }

    return jwt.encode(
        claims = encode,
        key = settings.auth_jwt.private_key.read_text(),
        algorithm = settings.auth_jwt.ALGORITHM,
    )


async def generate_token(email: str, password: str, db_session: AsyncSession) -> TokenResponseSchema:
    user = await authenticate_user(email, password, db_session)

    if not user:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = "Не правильный логин или пароль.",
            headers = {"Authorization": "Bearer"},
        )

    expires = timedelta(days=3)
    token = cteate_access_token(user, expires)

    return TokenResponseSchema(
        access_token = token,
        token_type = "Bearer"
    )


async def create_user(data: UserCreateSchema, db_session: AsyncSession):
    try:
        await UserRepository(db_session).create(data.model_dump())
    except IntegrityError:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = 'Email уже существует'
        )
    except Exception:
        raise


def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    credentials_exeption = HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail = "Невалидный токен",
        headers = {"Authorization": "Bearer"},
    )

    try:
        payload = jwt.decode(
            token = token,
            key = settings.auth_jwt.public_key.read_text(),
            algorithms = [settings.auth_jwt.ALGORITHM],
        )

        user_id = payload.get("id")

        if not user_id:
            raise credentials_exeption

        return UserAuthSchema(id = user_id)
    except JWTError:
        raise credentials_exeption
