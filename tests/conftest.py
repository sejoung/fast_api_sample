from __future__ import annotations

import os
import uuid

import pytest
from httpx import AsyncClient, ASGITransport
from testcontainers.mysql import MySqlContainer

from sejoung.application import APPCreator
from sejoung.configuration import log

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
        log.debug(f"Database URL: %s ", con_url)
        yield con_url


@pytest.fixture
def app(setup):
    app = APPCreator()
    return app


@pytest.fixture
async def client(app):
    await app.create_database()
    yield AsyncClient(transport=ASGITransport(app=app.get_app()), base_url="http://localhost")


@pytest.fixture
def generate_uuid():
    return uuid.uuid4()
