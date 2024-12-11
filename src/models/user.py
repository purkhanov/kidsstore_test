from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.models.base import Base
from src.models.cart import Cart


class User(Base):
    __tablename__ = "users"

    email: Mapped[str] = mapped_column(unique=True)
    name: Mapped[str]
    password: Mapped[str]

    cart: Mapped['Cart'] = relationship(back_populates='user')
