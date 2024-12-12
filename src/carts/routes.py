from typing import Annotated
from fastapi import APIRouter, status, Path, Query
from src.database.dependencies import db_dependency
from src.dependencies import user_dependency
from src.carts.service import CartService


router = APIRouter(prefix='/cart', tags=['cart'])


@router.get('', status_code=status.HTTP_200_OK)
async def get_carts(user: user_dependency, db: db_dependency):
    return await CartService(db).get_carts(user.id)



@router.post('/{product_id}', status_code=status.HTTP_201_CREATED)
async def add_to_cart(
    user: user_dependency,
    product_id: Annotated[int, Path(gt=0)],
    db: db_dependency
):
    quantity = 1
    await CartService(db).add_to_cart(user.id, product_id, quantity)


@router.put('/{product_id}', status_code=status.HTTP_202_ACCEPTED)
async def update_cart(
    user: user_dependency,
    product_id: Annotated[int, Path(gt=0)],
    quantity: Annotated[int, Query(gt=0)],
    db: db_dependency
):
    await CartService(db).update_cart(user.id, product_id, quantity)


@router.delete('/{product_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(
    user: user_dependency,
    product_id: Annotated[int, Path(gt=0)],
    db: db_dependency
):
    await CartService(db).delete_cart(user.id, product_id)
