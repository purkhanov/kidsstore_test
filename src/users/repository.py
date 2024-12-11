from sqlalchemy.exc import IntegrityError
from src.database.repositories import SQLAlchemyRepository
from src.database.models import User
from src.database.exceptions import AlreadyExists


class UserRepository(SQLAlchemyRepository):
    model = User


    async def create(self, data):
        try:
            return await super().create(data)
        except IntegrityError as e:
            raise AlreadyExists()
        except Exception as e:
            raise
