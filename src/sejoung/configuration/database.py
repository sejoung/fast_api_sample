import os
from contextlib import asynccontextmanager
from typing import Any, AsyncGenerator, Optional

from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession

from .logger import log


class Database:
    _INSTANCE:Optional["Database"] = None

    def __init__(self, db_url: str) -> None:
        if db_url is None:
            raise ValueError("db_url is required")
        log.debug("db_url %s", db_url)
        self.__engine = create_async_engine(
            db_url,
            echo=True,
            echo_pool=True,
            pool_recycle=10,
            pool_size=1,
            max_overflow=20,
            pool_timeout=3600,
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
        log.debug("Database dispose")
        await self.__engine.dispose()

    @classmethod
    def get_instance(cls) -> "Database":
        if cls._INSTANCE is not None:
            log.debug("Database instance already exists")
            return cls._INSTANCE
        else:
            log.debug("Database instance exists")
            db_url = os.getenv("DATABASE_URL")
            cls._INSTANCE = Database(db_url)
        return cls._INSTANCE

    @classmethod
    def remove_instance(cls) -> None:
        """
            테쇼트 용도로 사용 하려고 만듬
        """
        cls._INSTANCE = None
        log.debug("Database instance removed")
