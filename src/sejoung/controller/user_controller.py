import logging
from uuid import UUID

from fastapi import APIRouter

from sejoung.entities.user import UserResponse
from sejoung.service import UserService


class UserController:
    def __init__(self, logger: logging.Logger, user_service: UserService):
        self.__log = logger
        self.__user_service = user_service
        self.user_router = APIRouter(prefix="/users", tags=["Users"])
        self.user_router.add_api_route(
            "/", self.get_users, methods=["GET"], response_model=list[UserResponse]
        )
        self.user_router.add_api_route(
            "/{user_id}", self.get_user, methods=["GET"], response_model=UserResponse
        )

    async def get_users(self):
        self.__log.debug("retrieving all users")
        result = await  self.__user_service.get_users()
        self.__log.debug(result)
        return result

    async def get_user(self, user_id: str):
        result = await  self.__user_service.get_user(UUID(user_id))
        self.__log.debug(result)
        return result
