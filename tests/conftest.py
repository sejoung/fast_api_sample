import asyncio
import uuid

import pytest
from httpx import AsyncClient, ASGITransport
from testcontainers.mysql import MySqlContainer

from sejoung import app
from sejoung.configuration import log, Database


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture
def client():
    yield AsyncClient(transport=ASGITransport(app=app), base_url="http://localhost")


@pytest.fixture
def db_url():
    with  MySqlContainer("mariadb:10.5") as mariadb:
        db_url = mariadb._create_connection_url(dialect="mysql+aiomysql",
                                                username=mariadb.MYSQL_USER,
                                                password=mariadb.MYSQL_PASSWORD,
                                                db_name=mariadb.MYSQL_DATABASE,
                                                port=mariadb.port_to_expose)
        log.debug("db_url %s", db_url)
        return db_url


@pytest.fixture
async def session():
    with  MySqlContainer("mariadb:10.5") as mariadb:
        con_url = mariadb._create_connection_url(dialect="mysql+aiomysql",
                                                 username=mariadb.MYSQL_USER,
                                                 password=mariadb.MYSQL_PASSWORD,
                                                 db_name=mariadb.MYSQL_DATABASE,
                                                 port=mariadb.port_to_expose)
        log.debug("repository db_url %s", con_url)
        database = Database(db_url=con_url)
        await database.create_database()
        yield database.get_session


@pytest.fixture
def generate_uuid():
    return uuid.uuid4()
