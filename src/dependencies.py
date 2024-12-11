from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.database.base import get_db


db_dependency = Annotated[AsyncSession, Depends(get_db)]