import uuid
from typing import Annotated

from fastapi import Depends

from sejoung.configuration import log
from sejoung.exceptions.exceptions import UserNotFoundError
from sejoung.repositories.dependencies import get_user_repository
from sejoung.repositories.user_repository import UserRepository


class UserService:

    def __init__(self, user_repository: Annotated[UserRepository, Depends(get_user_repository)]):
        self.__user_repository = user_repository

    async def get_user(self, user_id: uuid.UUID):
        result = await self.__user_repository.find_one(user_id)
        if result is None:
            log.debug("user_id %s not found", user_id)
            raise UserNotFoundError(user_id)
        return result

    async def get_users(self):
        results = await self.__user_repository.find_all()
        if len(results) == 0:
            log.debug("No user found")
            return []
        return results
