from contextlib import contextmanager
from typing import Any, Generator

from sqlmodel import SQLModel, create_engine, Session


class Database:

    def __init__(self, db_url: str) -> None:
        self.__engine = create_engine(db_url, echo=True)

    def create_database(self) -> None:
        SQLModel.metadata.create_all(self.__engine)

    @contextmanager
    def get_session(self) -> Generator[Session, Any, None]:
        try:
            with Session(self.__engine) as session:
                yield session
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
