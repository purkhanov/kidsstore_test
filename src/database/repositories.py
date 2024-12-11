from typing import Any
from sqlalchemy import select, update, delete, Result
from sqlalchemy.ext.asyncio import AsyncSession


class SQLAlchemyRepository:
    model = None

    def __init__(self, session: AsyncSession) -> None:
        self.session = session


    async def create(self, data: dict[str, Any]) -> Any:
        new_data = self.model(**data)
        self.session.add(new_data)
        await self.session.commit()
        return new_data


    async def find_all(self) -> list[Any]:
        stmt = select(self.model)
        res: Result = await self.session.execute(stmt)
        return res.scalars().all()


    async def find_one(self, pk: int) -> Any | None:
        stmt = select(self.model).where(self.model.id == pk)
        res: Result = await self.session.execute(stmt)
        return res.scalar_one_or_none()
    

    async def update(self, pk: int, data: dict[str, Any]) -> Any:
        stmt = (
            update(self.model)
            .where(self.model.id == pk)
            .values(**data)
            .returning(self.model)
        )
        res: Result = await self.session.execute(stmt)
        await self.session.commit()
        return res.scalar()


    async def delete(self, pk: int) -> None:
        stmt = delete(self.model).where(self.model.id == pk)
        await self.session.execute(stmt)
        await self.session.commit()
