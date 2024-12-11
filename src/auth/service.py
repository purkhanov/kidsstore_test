from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from src.users.schemas import UserCreateSchema
from src.users.service import UserService


oauth2_bearer = OAuth2PasswordBearer(tokenUrl="/auth/token")


# async def generate_token(email: str, password: str, db_session: AsyncSession):
#     user: User | None = await AuthService().authenticate_user(
#         email, password, db_session
#     )

#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail="Не правильный логин или пароль.",
#             headers={"Authorization": "Bearer"},
#         )

#     if not user.is_active:
#         raise HTTPException(
#             status_code=status.HTTP_406_NOT_ACCEPTABLE,
#             detail="Ваш аккаунт не активирован",
#         )

#     token = AuthService().cteate_access_token(user)
#     return {"access_token": token, "token_type": "Bearer"}


async def authenticate_user():
    pass


async def create_user(data: UserCreateSchema, db_session: AsyncSession):
    try:
        await UserService(db_session).create_user(data)
    except IntegrityError:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = 'Email уже существует'
        )
    except Exception:
        raise


