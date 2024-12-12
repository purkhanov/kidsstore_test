from typing import Any
from sqlalchemy import select, update, delete, Result
from sqlalchemy.orm import aliased
from src.database.repositories import SQLAlchemyRepository
from src.database.models import Cart, Product


class CartRepository(SQLAlchemyRepository):
    model = Cart

    async def get_user_carts(self, user_id: int) -> dict[str, Any]:
        product = aliased(Product)

        stmt = (
            select(
                self.model.id,
                self.model.product_id.label('product_id'),
                self.model.quantity,
                product.name,
                product.price,
                product.description,
                product.category,
            )
            .where(self.model.user_id == user_id)
            .join(product, self.model.product_id == product.id)
        )
        res: Result = await self.session.execute(stmt)
        carts = res.fetchall()

        if not carts:
            return {}

        result = []
        total_price = 0
        for cart in carts:
            product = cart._asdict()
            total_price += product['price'] * product['quantity']
            result.append(product)
        
        return {'total_price': total_price, 'cart': result}
    

    async def get_product(self, user_id: int, product_id: int) -> Cart | None:
        stmt = (
            select(self.model)
            .where(
                self.model.user_id == user_id,
                self.model.product_id == product_id,
            )
        )
        res: Result = await self.session.execute(stmt)
        return res.scalar_one_or_none()
    

    async def add_to_cart(self, user_id: int, product_id: int, quantity: int):
        stmt = Cart(
            user_id = user_id,
            product_id = product_id,
            quantity = quantity,
        )
        self.session.add(stmt)
        await self.session.commit()

    
    async def update_cart(self, user_id: int, product_id: int, quantity: int) -> None:
        stmt = (
            update(self.model)
            .where(
                self.model.user_id == user_id,
                self.model.product_id == product_id,
            )
            .values(quantity = quantity)
        )
        await self.session.execute(stmt)
        await self.session.commit()

    
    async def delete_product_from_cart(self, user_id: int, product_id: int) -> None:
        stmt = (
            delete(self.model)
            .where(
                self.model.product_id == product_id,
                self.model.user_id == user_id,
            )
        )
        await self.session.execute(stmt)
        await self.session.commit()

    
    async def delete_user_cart(self, user_id: int) -> None:
        stmt = delete(self.model).where(self.model.user_id == user_id)
        await self.session.execute(stmt)
        await self.session.commit()
