import pytest

from sejoung.exceptions.exceptions import UserNotFoundError


@pytest.mark.asyncio
async def test_user_service_not_found(app, generate_uuid):
    service = app.get_container().user_service()
    with pytest.raises(UserNotFoundError):
        await service.get_user(generate_uuid)


@pytest.mark.asyncio
async def test_user_service_found(app):
    repository = app.get_container().user_repository()
    service = app.get_container().user_service()
    create_user = await repository.create("zolla@abc.com", "beni")

    actual = await service.get_user(create_user.id)

    assert actual.email == "zolla@abc.com"
    assert actual.name == "beni"
