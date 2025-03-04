import pytest
from fastapi.testclient import TestClient
from testcontainers.mysql import MySqlContainer

from sejoung import app
from sejoung.configuration.database import Database


@pytest.fixture(autouse=True)
def client():
    yield TestClient(app)


@pytest.fixture(autouse=True)
def session():
    with MySqlContainer("mariadb:10.5") as mariadb:
        database = Database(db_url=mariadb.get_connection_url())
        database.create_database()
        yield database.get_session
