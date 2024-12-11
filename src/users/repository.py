from src.database.repositories import SQLAlchemyRepository
from src.database.models import User


class UserRepository(SQLAlchemyRepository):
    model = User
