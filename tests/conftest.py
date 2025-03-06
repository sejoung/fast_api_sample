from __future__ import annotations

import os
import uuid

import pytest
from httpx import AsyncClient, ASGITransport
from sqlalchemy import create_engine
from testcontainers.mysql import MySqlContainer

from sejoung.application import create_app

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
        engine = create_engine(con_url, echo=True)
        yield engine

@pytest.fixture
async def create_table(setup):
    pass

@pytest.fixture
def app(create_table):
    return create_app()

@pytest.fixture
def client(app):
    yield AsyncClient(transport=ASGITransport(app=app), base_url="http://localhost")

@pytest.fixture
def generate_uuid():
    return uuid.uuid4()


