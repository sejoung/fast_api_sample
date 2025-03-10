from __future__ import annotations

import os
import uuid

import pytest
from httpx import AsyncClient, ASGITransport
from testcontainers.mysql import MySqlContainer

from sejoung.application import create_app
from sejoung.configuration import log, Database
from sejoung.configuration.dependencies import lifespan

ASYNC_MYSQL_DIALECT = "mysql+aiomysql"

@pytest.fixture
def setup(request):
    with MySqlContainer("mariadb:10.5") as mariadb:
        con_url = mariadb._create_connection_url(dialect=ASYNC_MYSQL_DIALECT,
                                                     username=mariadb.MYSQL_USER,
                                                     password=mariadb.MYSQL_PASSWORD,
                                                     db_name=mariadb.MYSQL_DATABASE,
                                                     port=mariadb.port_to_expose)
        os.environ["DATABASE_URL"] = con_url
        log.debug(f"Database URL: %s ",con_url)
        yield con_url

@pytest.fixture
async def create_table(setup):
    database = Database.get_instance()
    await database.create_database()
    await database.dispose()

@pytest.fixture
def app(create_table):
    return create_app(lifespan=lifespan)

@pytest.fixture
def client(app):
    yield AsyncClient(transport=ASGITransport(app=app), base_url="http://localhost")

@pytest.fixture
def generate_uuid():
    return uuid.uuid4()

@pytest.fixture(autouse=True)
def run_after_each_test():
    yield
    Database.remove_instance()
