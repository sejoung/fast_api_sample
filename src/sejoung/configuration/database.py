import os
from contextlib import asynccontextmanager
from typing import Any, AsyncGenerator

from sqlalchemy import create_engine
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
        self.__db_url = db_url
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

    def create_database(self) -> None:
        url = self.__db_url.replace("mysql+aiomysql", "mysql+pymysql")
        engine = create_engine(url, echo=True)
        SQLModel.metadata.create_all(engine)
        engine.dispose()

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

    async def close(self):
        log.debug("Database dispose")
        await self.__engine.dispose()
