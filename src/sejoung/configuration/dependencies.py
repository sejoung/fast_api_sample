import os
from contextlib import asynccontextmanager

from fastapi import FastAPI

from .database import Database
from .logger import log


@asynccontextmanager
async def lifespan(app: FastAPI):
    db_url = os.getenv("DATABASE_URL")
    database_instance = Database.get_instance()
    app.database = database_instance
    log.debug("Database URL: %s", db_url)
    yield
    await database_instance.dispose()

