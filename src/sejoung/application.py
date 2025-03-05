import uvicorn
from fastapi import FastAPI

from sejoung.controller import UserController


def create_app():
    fastapi_app = FastAPI()
    user_router = UserController().router
    fastapi_app.include_router(user_router)
    return fastapi_app


app = create_app()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
