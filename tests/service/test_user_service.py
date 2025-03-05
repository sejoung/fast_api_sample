import pytest

from sejoung.exceptions.exceptions import UserNotFoundError
from sejoung.repositories.user_repository import UserRepository
from sejoung.service.user_service import UserService


@pytest.mark.asyncio
async def test_user_service(session, generate_uuid):
    repository = UserRepository(session)
    service = UserService(repository)

    with pytest.raises(UserNotFoundError):
        await service.get_user(generate_uuid)
