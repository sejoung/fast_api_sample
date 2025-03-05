import pytest


@pytest.mark.asyncio
async def test_get(client):
    response = await client.get("/users")

    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
