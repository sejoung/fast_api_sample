import pytest

from sejoung.repositories.dependencies import get_user_repository


@pytest.mark.asyncio
async def test_user_repository(app):
    repository = get_user_repository()
    user = await repository.create("zolla@abc.com", "aaa")
    actual = await repository.find_one(user.id)
    assert actual is not None
    assert actual.email == "zolla@abc.com"
    assert actual.name == "aaa"


@pytest.mark.asyncio
async def test_create_user(app):
    repository = get_user_repository()
    user = await repository.create("zolla@abc.com", "beni")
    assert user.email == "zolla@abc.com"
    assert user.name == "beni"
    assert user.id is not None
