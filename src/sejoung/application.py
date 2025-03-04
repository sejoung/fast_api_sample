from fastapi import FastAPI

from sejoung.configuration.container import Container
from sejoung.controller import UserController


def create_app():
    fastapi_app = FastAPI()
    fastapi_app.container = Container()
    user_router = UserController().router
    fastapi_app.include_router(user_router)
    return fastapi_app


app = create_app()
