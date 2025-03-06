import os

from .database import Database


def get_database() -> Database:
    db_url = os.getenv("DATABASE_URL")
    _database = Database.get_instance(db_url)
    return _database
