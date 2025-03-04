from fastapi import APIRouter


class UserController:
    def __init__(self):
        self.router = APIRouter()
        self.router.add_api_route("/users", self.get_users, methods=["GET"])

    async def get_users(self):
        return {"message": "Hello World"}
