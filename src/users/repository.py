from sqlalchemy import select, Result
from pydantic import EmailStr
from src.database.repositories import SQLAlchemyRepository
from src.database.models import User


class UserRepository(SQLAlchemyRepository):
    model = User

    async def get_user_by_email(self, email: EmailStr) -> User | None:
        stmt = select(self.model).where(self.model.email == email)
        res: Result = await self.session.execute(stmt)
        return res.scalar_one_or_none()
