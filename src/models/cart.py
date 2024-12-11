from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.models.base import Base
from src.models.user import User


class Cart(Base):
    __tablename__ = "carts"

    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    user: Mapped['User'] = relationship(back_populates='cart')

    product_id: Mapped[int] = mapped_column(ForeignKey('products.id'))

    quantity: Mapped[int] = mapped_column(default=1)
