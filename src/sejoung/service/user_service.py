import uuid

from sejoung.configuration import log
from sejoung.entities.user import UserResponse
from sejoung.exceptions.exceptions import UserNotFoundError
from sejoung.repositories import UserRepository


class UserService:

    def __init__(self, user_repository: UserRepository):
        self.__user_repository = user_repository

    async def get_user(self, user_id: uuid.UUID):
        result = await self.__user_repository.find_one(user_id)

        if result is None:
            log.debug("user_id %s not found", user_id)
            raise UserNotFoundError(user_id)

        return UserResponse.model_validate(result)

    async def get_users(self):
        results = await self.__user_repository.find_all()
        if len(results) == 0:
            log.debug("No user found")
            return []

        return [UserResponse.model_validate(x) for x in results]
