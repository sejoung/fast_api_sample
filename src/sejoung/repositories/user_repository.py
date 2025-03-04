from contextlib import AbstractContextManager
from typing import Type, Callable, Sequence

from sqlmodel import Session, select

from sejoung.entities.user import User


class UserRepository:
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]):
        self.__session_factory = session_factory

    def find_one(self, user_id) -> Type[User] | None:
        with self.__session_factory() as session:
            statement = select(User).filter(User.id == user_id)
            return session.exec(statement).one_or_none()

    def find_all(self) -> Sequence[User]:
        with self.__session_factory() as session:
            statement = select(User)
            return session.exec(statement).all()

    def create(self, user_id: str, name: str) -> User:
        with self.__session_factory() as session:
            user = User(user_id=user_id, name=name)
            session.add(user)
            session.commit()
            session.refresh(user)
            return user
