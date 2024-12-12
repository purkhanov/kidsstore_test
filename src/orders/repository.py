from typing import Any
from sqlalchemy import select, Result
from src.database.repositories import SQLAlchemyRepository
from src.database.models import Order


class OrderRepository(SQLAlchemyRepository):
    model = Order

    async def get_user_orders(self, user_id: int) -> list[Order]:
        stmt = (
            select(self.model)
            .where(self.model.user_id == user_id)
        )
        res: Result = await self.session.execute(stmt)
        return res.scalars().all()
