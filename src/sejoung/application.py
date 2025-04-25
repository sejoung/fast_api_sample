import os

import uvicorn
from fastapi import FastAPI

from sejoung.configuration.containers import Container


class APPCreator:
    def __init__(self):
        self.__app = FastAPI()
        self.__container = Container()

    def get_app(self):
        return self.__app

    def get_container(self):
        return self.__container

    async def create_database(self):
        await self.__container.db.provided.create_database()


if __name__ == "__main__":
    os.environ["DATABASE_URL"] = "mysql+aiomysql://root:root@localhost:3306/test"
    app = APPCreator()
    uvicorn.run(app.get_app(), host="0.0.0.0", port=8000)
