from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends

from sejoung.configuration import log
from sejoung.service.dependencies import get_user_service
from sejoung.service.user_service import UserService


class UserController:
    def __init__(self, user_service: Annotated[UserService, Depends(get_user_service)]):
        self.router = APIRouter()
        self.router.add_api_route("/users", self.get_users, methods=["GET"])
        self.__user_service = user_service

    async def get_users(self):
        log.debug("Hello World")
        result = await self.__user_service.get_users()
        log.debug(result)
        return {"message": "Hello World"}

    async def get_user(self, user_id: UUID):
        log.debug("Hello World")
        result = await self.__user_service.get_user(user_id)
        log.debug(result)
        return result
