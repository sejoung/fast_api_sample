from __future__ import annotations

import os
import uuid

import pytest
from _pytest.fixtures import FixtureLookupError
from httpx import AsyncClient, ASGITransport
from testcontainers.mysql import MySqlContainer

from sejoung.application import APPCreator
from sejoung.configuration import log

ASYNC_MYSQL_DIALECT = "mysql+aiomysql"


@pytest.fixture(scope="session")
def setup(request):
    with MySqlContainer("mariadb:10.5") as mariadb:
        con_url = mariadb._create_connection_url(dialect=ASYNC_MYSQL_DIALECT,
                                                 username=mariadb.MYSQL_USER,
                                                 password=mariadb.MYSQL_PASSWORD,
                                                 db_name=mariadb.MYSQL_DATABASE,
                                                 port=mariadb.port_to_expose)
        os.environ["DATABASE_URL"] = con_url
        log.debug("Database URL: %s ", con_url)
        yield con_url


@pytest.fixture
async def app(setup):
    app = APPCreator()
    app.get_container().database().create_database()
    yield app
    await app.get_container().database().close()


@pytest.fixture(autouse=True)
def inject_components(app, request) -> None:
    test_container = app.get_container()
    item = request._pyfuncitem  # noqa
    fixture_names = getattr(item, "fixturenames", request.fixturenames)
    for arg_name in fixture_names:
        try:
            request.getfixturevalue(arg_name)
        except FixtureLookupError as e:
            if arg_name == "inject_components":
                continue
            provided = test_container
            for seg in arg_name.split("__"):
                try:
                    provided = getattr(provided, seg)()
                except AttributeError:
                    raise e
            item.funcargs[arg_name] = provided


@pytest.fixture
def client(app):
    yield AsyncClient(transport=ASGITransport(app=app.get_app()), base_url="http://localhost")


@pytest.fixture
def generate_uuid():
    return uuid.uuid4()
