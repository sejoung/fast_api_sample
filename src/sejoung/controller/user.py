from dependency_injector.wiring import inject
from fastapi import APIRouter

from sejoung.repositories.user import UserRepository


class UserController:
    @inject
    def __init__(self, user_repository: UserRepository):
        self.__user_repository = user_repository
        self.router = APIRouter()
        self.router.add_api_route("/users", self.get_users, methods=["GET"])

    async def get_users(self) -> dict:
        users = self.__user_repository.get_user(1)
        return {"message": "Hello World"}
