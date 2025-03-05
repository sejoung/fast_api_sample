from sejoung.configuration import log
from sejoung.exceptions.exceptions import UserNotFoundError
from sejoung.repositories.user_repository import UserRepository


class UserService:

    def __init__(self, user_repository: UserRepository):
        self.__user_repository = user_repository

    async def get_user(self, user_id):
        result = await self.__user_repository.find_one(user_id)
        if result is None:
            log.debug("user_id %s not found", user_id)
            raise UserNotFoundError(user_id)
        return result
