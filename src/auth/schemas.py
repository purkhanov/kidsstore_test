from datetime import datetime
from typing import Annotated
from pydantic import BaseModel, Field, AfterValidator, StringConstraints, EmailStr
from passlib.context import CryptContext


class TokenResponseSchema(BaseModel):
    access_token: str
    token_type: str
