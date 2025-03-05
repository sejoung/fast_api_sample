from .database import Database
from .logger import log


def get_database() -> Database:
    db_url = "mysql+aiomysql://root:root@localhost:3306/test"
    _database = Database(db_url)
    log.debug("test %s", db_url)
    return _database
