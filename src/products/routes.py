from typing import Annotated
from fastapi import APIRouter, status, Path
from src.database.dependencies import db_dependency
from src.products.service import ProductService
from src.products.schemas import ProductsCreateSchema, ProductsUpdateSchema


router = APIRouter(prefix='/products', tags=['product'])


@router.get('', status_code=status.HTTP_200_OK)
async def get_products(db: db_dependency):
    return await ProductService(db).get_products()


@router.get('/{product_id}', status_code=status.HTTP_200_OK)
async def get_product(
    product_id: Annotated[int, Path(gt=0)],
    db: db_dependency
):
    return await ProductService(db).get_product(product_id)


@router.post('', status_code=status.HTTP_201_CREATED)
async def create_product(data: ProductsCreateSchema, db: db_dependency):
    await ProductService(db).create_product(data)


@router.put('/{product_id}', status_code=status.HTTP_202_ACCEPTED)
async def update_product(
    product_id: Annotated[int, Path(gt=0)],
    data: ProductsUpdateSchema,
    db: db_dependency
):
    await ProductService(db).update_product(product_id, data)


@router.delete('/{product_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(
    product_id: Annotated[int, Path(gt=0)],
    db: db_dependency
):
    return await ProductService(db).delete_product(product_id)
