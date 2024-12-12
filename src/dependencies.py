from typing import Annotated
from fastapi import Depends
from src.auth.schemas import UserAuthSchema
from src.auth.service import get_current_user


user_dependency = Annotated[UserAuthSchema, Depends(get_current_user)]
