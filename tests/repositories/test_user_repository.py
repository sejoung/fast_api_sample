import pytest


@pytest.mark.asyncio
async def test_user_repository(app):
    repository = app.get_container().user_repository.provided
    user = await repository.create("zolla@abc.com", "aaa")
    actual = await repository.find_one(user.id)
    assert actual is not None
    assert actual.email == "zolla@abc.com"
    assert actual.name == "aaa"


@pytest.mark.asyncio
async def test_create_user(app):
    repository = app.get_container().user_repository.provided
    user = await repository.create("zolla@abc.com", "beni")
    assert user.email == "zolla@abc.com"
    assert user.name == "beni"
    assert user.id is not None
