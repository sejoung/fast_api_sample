from __future__ import annotations

from sejoung.configuration import Database


def get_database() -> Database:
    _database = Database("mysql+aiomysql://root:root@localhost:3306/test")
    return _database
