from contextlib import AbstractContextManager
from typing import Type, Callable, Sequence

from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from sejoung.entities.user import User


class UserRepository:
    def __init__(self, session_factory: Callable[..., AbstractContextManager[AsyncSession]]):
        self.__session_factory = session_factory

    async def find_one(self, user_id) -> Type[User] | None:
        async with self.__session_factory() as session:
            statement = select(User).where(User.id == user_id)
            response = await session.exec(statement)
            return response.first()

    async def find_all(self) -> Sequence[User]:
        async with self.__session_factory() as session:
            statement = select(User)
            response = await session.exec(statement)
            return response.all()

    async def create(self, __email: str, __name: str) -> User:
        async with self.__session_factory() as session:
            user = User(email=__email, name=__name)
            session.add(user)
            await session.commit()
            await session.refresh(user)
            return user
