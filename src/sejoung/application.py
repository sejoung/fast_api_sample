import uvicorn
from fastapi import FastAPI

from sejoung.controller import UserController
from sejoung.service import get_user_service


def create_app():
    fastapi_app = FastAPI()
    user_router = UserController(get_user_service()).router
    fastapi_app.include_router(user_router)
    return fastapi_app



if __name__ == "__main__":
    app = create_app()
    uvicorn.run(app, host="0.0.0.0", port=8000)
