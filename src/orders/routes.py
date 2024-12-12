from fastapi import APIRouter, status
from src.database.dependencies import db_dependency
from src.dependencies import user_dependency
from src.orders.service import OrderService


router = APIRouter(tags=['order'])


@router.get('/orders', status_code=status.HTTP_200_OK)
async def get_orders(user: user_dependency, db: db_dependency):
    return await OrderService(db).get_orders(user.id)


@router.post('/checkout', status_code=status.HTTP_201_CREATED)
async def add_to_cart(user: user_dependency, db: db_dependency):
    await OrderService(db).create_order(user.id)
