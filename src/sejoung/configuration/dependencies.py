import os

from .database import Database
from .logger import log


def get_database() -> Database:
    db_url =os.getenv("DATABASE_URL")
    _database = Database(db_url)
    log.debug("test %s", db_url)
    return _database
