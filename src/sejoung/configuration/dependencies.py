from contextlib import asynccontextmanager

from fastapi import FastAPI

from .database import Database


@asynccontextmanager
async def lifespan(app: FastAPI):
    database_instance = Database.get_instance()
    yield
    await database_instance.dispose()
