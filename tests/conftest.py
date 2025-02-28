import pytest
from fastapi.testclient import TestClient

from sejoung.application import app


@pytest.fixture(scope="function", autouse=True)
def client():
    yield TestClient(app)
