import pytest

from sejoung.exceptions.exceptions import UserNotFoundError
from sejoung.repositories import UserRepository
from sejoung.service import UserService


@pytest.mark.asyncio
async def test_user_service_not_found(session, generate_uuid):
    repository = UserRepository(session)
    service = UserService(repository)

    with pytest.raises(UserNotFoundError):
        await service.get_user(generate_uuid)


@pytest.mark.asyncio
async def test_user_service_found(session):
    repository = UserRepository(session)
    service = UserService(repository)
    create_user = await repository.create("zolla@abc.com", "beni")

    actual = await service.get_user(create_user.id)

    assert actual.email == "zolla@abc.com"
    assert actual.name == "beni"
