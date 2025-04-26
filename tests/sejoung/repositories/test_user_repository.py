import pytest

from sejoung.repositories import UserRepository


@pytest.mark.asyncio
async def test_user_repository(user_repository: UserRepository):
    user = await user_repository.create("zolla@abc.com", "aaa")
    actual = await user_repository.find_one(user.id)
    assert actual is not None
    assert actual.email == "zolla@abc.com"
    assert actual.name == "aaa"


@pytest.mark.asyncio
async def test_create_user(user_repository: UserRepository):
    user = await user_repository.create("zolla@abc.com", "beni")
    assert user.email == "zolla@abc.com"
    assert user.name == "beni"
    assert user.id is not None
