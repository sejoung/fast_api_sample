import os

import uvicorn
from fastapi import FastAPI

from sejoung.configuration.containers import Container


class APPCreator:
    def __init__(self):
        self.__app = FastAPI()
        self.__container = Container()
        self.__app.include_router(self.__container.user_controller().user_router)

    def get_app(self):
        return self.__app

    def get_container(self):
        return self.__container


if __name__ == "__main__":
    os.environ["DATABASE_URL"] = "mysql+aiomysql://root:root@localhost:3306/test"
    app = APPCreator()
    app.get_container().database().create_database()
    uvicorn.run(app.get_app(), host="0.0.0.0", port=8000)
