from sqlalchemy.ext.asyncio import AsyncSession
from src.products.repository import ProductRepository
from src.database.models import Product
from src.products.schemas import ProductsCreateSchema, ProductsUpdateSchema


class ProductService:
    def __init__(self, db_session: AsyncSession):
        self.repos: ProductRepository = ProductRepository(db_session)


    async def get_products(self) -> list[Product]:
        return await self.repos.find_all()
    

    async def get_product(self, product_id: int) -> Product:
        return await self.repos.find_one(product_id)
    

    async def create_product(self, data: ProductsCreateSchema) -> Product:
        return await self.repos.create(data.model_dump())
    

    async def update_product(self,product_id: int, data: ProductsUpdateSchema) -> Product:
        return await self.repos.update(product_id, data.model_dump(exclude_none=True))
    

    async def delete_product(self, product_id: int) -> None:
        return await self.repos.delete(product_id)
