from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends

from sejoung.configuration import log
from sejoung.entities.user import UserResponse
from sejoung.service import UserService
from sejoung.service.dependencies import get_user_service


class UserController:
    def __init__(self):
        self.user_router = APIRouter(prefix="/users", tags=["Users"])
        self.user_router.add_api_route(
            "/", self.get_users, methods=["GET"], response_model=list[UserResponse]
        )
        self.user_router.add_api_route(
            "/{user_id}", self.get_user, methods=["GET"], response_model=UserResponse
        )

    async def get_users(
        self, user_service: Annotated[UserService, Depends(get_user_service)]
    ):
        log.debug("retrieving all users")
        result = await user_service.get_users()
        log.debug(result)
        return result

    async def get_user(
        self,
        user_id: str,
        user_service: Annotated[UserService, Depends(get_user_service)],
    ):
        result = await user_service.get_user(UUID(user_id))
        log.debug(result)
        return result
