import pytest

from sejoung.exceptions.exceptions import UserNotFoundError
from sejoung.repositories import get_user_repository
from sejoung.service import get_user_service


@pytest.mark.asyncio
async def test_user_service_not_found(app, generate_uuid):
    service = get_user_service()
    with pytest.raises(UserNotFoundError):
        await service.get_user(generate_uuid)


@pytest.mark.asyncio
async def test_user_service_found(app):
    repository = get_user_repository()
    service = get_user_service()
    create_user = await repository.create("zolla@abc.com", "beni")

    actual = await service.get_user(create_user.id)

    assert actual.email == "zolla@abc.com"
    assert actual.name == "beni"
