import pytest

from sejoung.configuration.database import AsyncDatabase
from sejoung.entities import User
from sejoung.exceptions.exceptions import UserNotFoundError
from sejoung.service import UserService


@pytest.mark.asyncio
async def test_user_service_not_found(user_service: UserService, generate_uuid):
    with pytest.raises(UserNotFoundError):
        await user_service.get_user(generate_uuid)


@pytest.mark.asyncio
async def test_user_service_found(user_service: UserService,
                                  database: AsyncDatabase,
                                  generate_uuid):
    async with database.session() as session:
        create_user = User(id=generate_uuid, name="beni", email="zolla@abc.com")
        session.add(create_user)

        actual = await user_service.get_user(create_user.id)
        assert actual.email == "zolla@abc.com"
        assert actual.name == "beni"
