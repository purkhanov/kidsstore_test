from typing import Annotated
from pydantic import BaseModel, StringConstraints, AfterValidator, Field, EmailStr
from passlib.context import CryptContext


bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

HASH_PASS = Annotated[
    str,
    StringConstraints(strip_whitespace=True),
    Field(min_length=6),
    AfterValidator(lambda passw: bcrypt_context.hash(passw)),
]
NAME = Annotated[
    str,
    StringConstraints(strip_whitespace=True),
    Field(min_length=3, max_length=50),
]


class UserResponseSchema(BaseModel):
    email: EmailStr
    name: NAME


class UserCreateSchema(BaseModel):
    email: EmailStr
    name: NAME
    password: HASH_PASS


class UserUpdateSchema(BaseModel):
    email: EmailStr | None = None
    name: NAME | None = None
    password: HASH_PASS | None = None
