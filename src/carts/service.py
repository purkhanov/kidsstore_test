from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from src.carts.repository import CartRepository
from src.products.repository import ProductRepository
from src.database.models import Cart, Product


class CartService:
    def __init__(self, db_session: AsyncSession):
        self.repos = CartRepository(db_session)
        self.product_repos = ProductRepository(db_session)


    async def get_carts(self, user_id: InterruptedError) -> list[Cart]:
        return await self.repos.get_user_carts(user_id)
    

    async def add_to_cart(self, user_id: int, product_id: int, quantity: int):
        product = await self.product_repos.find_one(product_id)
        product_in_cart = await self.repos.get_product(user_id, product_id)

        if product_in_cart:
            raise HTTPException(
                status_code = status.HTTP_400_BAD_REQUEST,
                detail = "Товар уже добавлен в корзину"
            )

        if not product or product.in_stock < 1:
            raise HTTPException(
                status_code = status.HTTP_400_BAD_REQUEST,
                detail = "Товар нет на складе"
            )

        await self.repos.add_to_cart(user_id, product_id, quantity)


    async def update_cart(self, user_id: int, product_id: int, quantity: int) -> None:
        await self.repos.update_cart(user_id, product_id, quantity)
    

    async def delete_cart(self, user_id: int, product_id: int) -> None:
        await self.repos.delete_from_cart(user_id, product_id)
