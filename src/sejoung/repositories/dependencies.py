from __future__ import annotations

from sejoung.configuration.dependencies import get_database
from sejoung.repositories.user_repository import UserRepository


def get_user_repository() -> UserRepository:
    return UserRepository(get_database().get_session)
