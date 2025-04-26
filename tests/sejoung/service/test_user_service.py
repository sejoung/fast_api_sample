import pytest

from sejoung.exceptions.exceptions import UserNotFoundError
from sejoung.repositories import UserRepository
from sejoung.service import UserService


@pytest.mark.asyncio
async def test_user_service_not_found(user_service: UserService, generate_uuid):
    with pytest.raises(UserNotFoundError):
        await user_service.get_user(generate_uuid)


@pytest.mark.asyncio
async def test_user_service_found(user_service: UserService, user_repository: UserRepository):
    create_user = await user_repository.create("zolla@abc.com", "beni")

    actual = await user_service.get_user(create_user.id)

    assert actual.email == "zolla@abc.com"
    assert actual.name == "beni"
