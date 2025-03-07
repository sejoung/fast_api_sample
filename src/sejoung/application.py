import os

import uvicorn
from fastapi import FastAPI

from sejoung.configuration.dependencies import lifespan
from sejoung.controller import UserController


def create_app(lifespan):
    fastapi_app = FastAPI(lifespan=lifespan)
    fastapi_app.include_router(UserController().user_router)
    return fastapi_app

if __name__ == "__main__":
    os.environ["DATABASE_URL"] = "mysql+aiomysql://root:root@localhost:3306/test"
    app = create_app(lifespan)
    uvicorn.run(app, host="0.0.0.0", port=8000)
