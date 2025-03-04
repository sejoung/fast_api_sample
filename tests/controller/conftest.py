import pytest
from fastapi.testclient import TestClient
from testcontainers.mysql import MySqlContainer

from sejoung import app
from sejoung.configuration.database import Database


@pytest.fixture(scope="function", autouse=True)
def mariadb():
    with MySqlContainer("mariadb:10.5") as mariadb:
        yield mariadb


@pytest.fixture(scope="function", autouse=True)
def client(mariadb):
    database = Database(db_url=mariadb.get_connection_url())
    database.create_database()
    app.container.database.override(database)
    yield TestClient(app)
