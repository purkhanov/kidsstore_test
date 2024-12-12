from enum import Enum
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase


class Status(Enum):
    created = 'created'
    pending = 'pending'


class BaseModel(AsyncAttrs, DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True, index=True)


class Product(BaseModel):
    __tablename__ = "products"

    name: Mapped[str]
    price: Mapped[int]
    description: Mapped[str | None]
    category: Mapped[str]
    in_stock: Mapped[int] = mapped_column(default=0)


class User(BaseModel):
    __tablename__ = "users"

    email: Mapped[str] = mapped_column(unique=True)
    name: Mapped[str]
    password: Mapped[str]

    carts: Mapped[list['Cart']] = relationship(back_populates='user')
    orders: Mapped[list['Orders']] = relationship(back_populates='user')


class Cart(BaseModel):
    __tablename__ = "carts"

    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    user: Mapped['User'] = relationship(back_populates='carts')

    product_id: Mapped[int] = mapped_column(ForeignKey('products.id'))

    quantity: Mapped[int] = mapped_column(default=0)



class Orders(BaseModel):
    __tablename__ = "orders"

    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    user: Mapped['User'] = relationship(back_populates='orders')

    total_price: Mapped[int]
    status: Mapped[str]
