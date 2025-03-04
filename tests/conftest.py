import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from testcontainers.mysql import MySqlContainer

from sejoung import app
from sejoung.configuration.database import Base


@pytest.fixture(scope="function", autouse=True)
def client():
    yield TestClient(app)


@pytest.fixture(scope="function", autouse=True)
def session():
    with MySqlContainer("mariadb:10.5") as mariadb:
        engine = create_engine(mariadb.get_connection_url(), echo=True)
        Base.metadata.create_all(engine)
        Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        with Session() as session:
            try:
                yield session
            finally:
                session.rollback()
                session.close()
