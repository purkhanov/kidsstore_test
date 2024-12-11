from src.database.repositories import SQLAlchemyRepository
from src.database.models import Product


class ProductRepository(SQLAlchemyRepository):
    model = Product