import pytest

from sejoung.repositories import get_user_repository


@pytest.mark.asyncio
async def test_user_repository(setup,generate_uuid):
    repository = get_user_repository()
    await repository.find_all()
    actual = await repository.find_one(generate_uuid)
    assert actual is None


@pytest.mark.asyncio
async def test_create_user(setup):
    repository = get_user_repository()
    user = await repository.create("zolla@abc.com", "beni")
    assert user.email == "zolla@abc.com"
    assert user.name == "beni"
    assert user.id is not None
