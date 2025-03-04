import pytest
from fastapi.testclient import TestClient

from sejoung import app


@pytest.fixture(scope="function", autouse=True)
def client():
    yield TestClient(app)
