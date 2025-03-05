from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends

from sejoung.configuration import log
from sejoung.entities.user import UserResponse
from sejoung.service import UserService
from sejoung.service import get_user_service


class UserController:
    def __init__(self, user_service: Annotated[UserService, Depends(get_user_service)]):
        self.router = APIRouter()
        self.router.add_api_route("/users", self.get_users, methods=["GET"], response_model=list[UserResponse])
        self.router.add_api_route("/users/{user_id}", self.get_user, methods=["GET"], response_model=UserResponse)
        self.__user_service = user_service

    async def get_users(self):
        result = await self.__user_service.get_users()
        log.debug(result)
        return result

    async def get_user(self, user_id: str):
        result = await self.__user_service.get_user(UUID(user_id))
        log.debug(result)
        return result
