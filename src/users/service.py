from sqlalchemy.ext.asyncio import AsyncSession
from src.users.repository import UserRepository
from src.database.models import User
from src.users.schemas import UserCreateSchema, UserUpdateSchema


class UserService:
    def __init__(self, db_session: AsyncSession):
        self.repos: UserRepository = UserRepository(db_session)


    async def get_user(self, user_id: int) -> User:
        return await self.repos.find_one(user_id)


    async def create_user(self, data: UserCreateSchema) -> User:
        return await self.repos.create(data.model_dump())


    async def update_user(self, user_id: int, data: UserUpdateSchema) -> User:
        return await self.repos.update(user_id, data.model_dump(exclude_none=True))


    async def delete_user(self, user_id: int) -> None:
        return await self.repos.delete(user_id)
