from contextlib import AbstractContextManager
from typing import Type, Callable

from sqlalchemy.orm import Session

from sejoung.entities.user import User


class UserRepository:
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]):
        self.__session_factory = session_factory

    def get_user(self, user_id) -> Type[User] | None:
        with self.__session_factory() as session:
            return session.query(User).filter(User.id == user_id).first()
