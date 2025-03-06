from contextlib import asynccontextmanager
from typing import Any, AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession

from .logger import log


class Database:

    def __init__(self, db_url: str) -> None:
        if db_url is None:
            raise ValueError("db_url is required")
        log.debug("db_url %s", db_url)
        self.__engine = create_async_engine(
            db_url,
            echo=True,
            echo_pool=True,
            pool_recycle=60,
            pool_size=1,
            max_overflow=5,
            pool_timeout=50,
            isolation_level="READ COMMITTED",
        )

    async def create_database(self) -> None:
        async with self.__engine.begin() as conn:
            await conn.run_sync(SQLModel.metadata.create_all)

    @asynccontextmanager
    async def get_session(self) -> AsyncGenerator[AsyncSession, Any]:
        try:
            async with AsyncSession(self.__engine) as session:
                yield session
        except Exception as e:
            await session.rollback()
            raise e
        finally:
            await session.close()
            await self.__engine.dispose()

    async def dispose(self):
        await self.__engine.dispose()
