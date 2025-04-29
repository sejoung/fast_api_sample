import logging
import os
from asyncio import current_task
from contextlib import asynccontextmanager
from typing import Any, AsyncGenerator

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncEngine,
    async_sessionmaker,
    async_scoped_session,
)
from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession


class AsyncDatabase:

    def __init__(self, logger: logging.Logger) -> None:
        self.__log = logger

        db_url = os.getenv("DATABASE_URL")
        if not db_url:
            raise ValueError("DATABASE_URL must be set in environment variables.")
        self.__db_url = db_url
        self.__log.debug("DATABASE_URL: %s", db_url)

        self._engine: AsyncEngine = create_async_engine(
            db_url,
            echo=True,
            pool_pre_ping=True,
            pool_recycle=1800,
            pool_size=5,
            max_overflow=10,
            isolation_level="READ COMMITTED",
        )

        # expire_on_commit=False 설정! (DetachedInstanceError 방지)
        self._session_factory = async_scoped_session(
            scopefunc=current_task,
            session_factory=async_sessionmaker(
                self._engine,
                expire_on_commit=False,
                class_=AsyncSession,
                autocommit=False,
            ),
        )

        self._is_test = os.getenv("IS_TEST", "false").lower() == "true"
        self.__log.debug("IS_TEST Mode: %s", self._is_test)

    def create_database(self) -> None:
        url = self.__db_url.replace("mysql+aiomysql", "mysql+pymysql")
        engine = create_engine(url, echo=True)
        SQLModel.metadata.create_all(engine)
        engine.dispose()

    @asynccontextmanager
    async def session(self) -> AsyncGenerator[AsyncSession, Any]:
        async with self._session_factory() as session:
            try:
                async with session.begin() as transaction:
                    self.__log.debug("Session started")
                    self.__log.debug("Session ID: %s", id(session))
                    yield session
                    await transaction.commit()
            except Exception as e:
                self.__log.exception("Session error occurred, rolling back...")
                await session.rollback()
                raise e
            finally:
                await session.close()

    async def close(self) -> None:
        self.__log.debug("Disposing database engine...")
        await self._engine.dispose()
