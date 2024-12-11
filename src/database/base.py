from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from ..config import settings


engine = create_async_engine(
    url = settings.db.DB_URL,
    echo = settings.db.ECHO
)

async_session = async_sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    db = async_session()

    try:
        yield db
    finally:
        await db.close()
