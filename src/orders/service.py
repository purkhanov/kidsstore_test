from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from src.orders.repository import OrderRepository
from src.carts.repository import CartRepository
from src.database.models import Cart


class OrderService:
    def __init__(self, db_session: AsyncSession):
        self.repos = OrderRepository(db_session)
        self.cart_repos = CartRepository(db_session)


    async def get_orders(self, user_id: int) -> list[Cart]:
        return await self.repos.get_user_orders(user_id)


    async def create_order(self, user_id: int) -> None:
        carts = await self.cart_repos.get_user_carts(user_id)
        total_price = carts.get('total_price', None)

        if not total_price:
            raise HTTPException(
                status_code = status.HTTP_400_BAD_REQUEST,
                detail = 'Корзина пуста',
            )
        
        data = {
            'user_id': user_id,
            'total_price': total_price
        }

        await self.repos.create(data)
        await self.cart_repos.delete_user_cart(user_id)
