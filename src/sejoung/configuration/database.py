import asyncio
from contextlib import asynccontextmanager
from typing import Any, AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession

from .logger import log


class Database:
    __instance = None

    def __init__(self, db_url: str) -> None:
        if db_url is None:
            raise ValueError("db_url is required")
        log.debug("db_url %s", db_url)
        if Database.__instance is None:
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
            await self.create_database()
            async with AsyncSession(self.__engine) as session:
                yield session
        except Exception as e:
            await session.rollback()
            raise e
        finally:
            await session.close()

    def __del__(self):
        asyncio.run(self.__engine.dispose())

    @classmethod
    def get_instance(cls, db_url: str) -> "Database":
        if not cls.__instance:
            cls.__instance = Database(db_url)
        return cls.__instance
