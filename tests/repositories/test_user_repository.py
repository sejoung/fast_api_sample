import pytest

from sejoung.repositories.user_repository import UserRepository

@pytest.mark.asyncio
async def test_user_repository(session, generate_uuid):
    repository = UserRepository(session)
    actual = await repository.find_one(generate_uuid)
    assert actual is None

@pytest.mark.asyncio
async def test_create_user(session):
    repository = UserRepository(session)
    user = await repository.create("zolla@abc.com", "beni")
    assert user.email == "zolla@abc.com"
    assert user.name == "beni"
    assert user.id is not None
