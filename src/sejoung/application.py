from fastapi import FastAPI

from sejoung.controller.user import UserController


def create_app():
    fastapi_app = FastAPI()
    user_router = UserController().router
    fastapi_app.include_router(user_router)
    return fastapi_app


app = create_app()
