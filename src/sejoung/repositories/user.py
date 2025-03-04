from contextlib import AbstractContextManager
from typing import Type, Callable

from sqlalchemy.orm import Session

from sejoung.entities.user import User


class UserRepository:
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]):
        self.__session_factory = session_factory

    def find_one(self, user_id) -> Type[User] | None:
        with self.__session_factory() as session:
            user = session.query(User).filter(User.id == user_id).one_or_none()
            return user

    def find_all(self) -> list[Type[User]]:
        with self.__session_factory() as session:
            return session.query(User).all()

    def create(self, user_id: str, name: str) -> Type[User]:
        with self.__session_factory() as session:
            user = User(user_id=user_id, name=name)
            session.add(user)
            session.commit()
            session.refresh(user)
            return user
