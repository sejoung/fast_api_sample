from fastapi import APIRouter

from sejoung.configuration import log


class UserController:
    def __init__(self):
        self.router = APIRouter()
        self.router.add_api_route("/users", self.get_users, methods=["GET"])

    async def get_users(self):
        log.debug("Hello World")
        return {"message": "Hello World"}
