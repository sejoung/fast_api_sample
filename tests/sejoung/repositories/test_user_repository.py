import pytest

from sejoung.configuration.database import AsyncDatabase
from sejoung.entities import User
from sejoung.repositories import UserRepository


@pytest.mark.asyncio
async def test_user_repository(user_repository: UserRepository, database: AsyncDatabase, generate_uuid):
    async with database.session() as session:
        user = User(id=generate_uuid, name="aaa", email="zolla@abc.com")
        session.add(user)
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
