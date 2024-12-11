from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase


class BaseModel(AsyncAttrs, DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True, index=True)


class Product(BaseModel):
    __tablename__ = "products"

    name: Mapped[str]
    price: Mapped[int]
    description: Mapped[str | None]
    category: Mapped[str]

