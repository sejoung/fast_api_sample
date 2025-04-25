import os
from contextlib import asynccontextmanager
from typing import Any, AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession

from .logger import log


class Database:

    def __init__(self) -> None:
        db_url = os.getenv("DATABASE_URL")
        if db_url is None:
            raise ValueError("db_url is required")
        log.debug("db_url %s", db_url)
        self.__engine = create_async_engine(
            db_url,
            echo=True,
            echo_pool=True,
            pool_recycle=100,
            pool_size=1,
            max_overflow=20,
            pool_timeout=30,
            pool_pre_ping=True,
            isolation_level="READ COMMITTED",
        )

    async def create_database(self) -> None:
        async with self.__engine.begin() as conn:
            await conn.run_sync(SQLModel.metadata.create_all)

    @asynccontextmanager
    async def session(self) -> AsyncGenerator[AsyncSession, Any]:
        try:
            async with AsyncSession(self.__engine) as session:
                yield session
        except Exception as e:
            await session.rollback()
            raise e
        finally:
            await session.close()

    async def dispose(self):
        log.debug("Database dispose")
        await self.__engine.dispose()
