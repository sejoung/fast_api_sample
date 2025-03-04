import logging
from contextlib import contextmanager
from typing import Any, Generator

from sqlalchemy import create_engine, orm
from sqlalchemy.orm import Session, declarative_base

logger = logging.getLogger(__name__)

Base = declarative_base()


class Database:

    def __init__(self, db_url: str) -> None:
        self.__engine = create_engine(db_url, echo=True)
        self.__session_factory = orm.scoped_session(
            orm.sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=self.__engine,
            ),
        )

    def create_database(self) -> None:
        Base.metadata.create_all(self.__engine)

    @contextmanager
    def get_session(self) -> Generator[Session, Any, None]:
        session: Session = self.__session_factory()
        try:
            yield session
        except Exception:
            logger.exception("Session rollback because of exception")
            session.rollback()
            raise Exception("Session rollback because of exception")
        finally:
            session.close()
