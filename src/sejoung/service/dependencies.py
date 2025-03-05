from __future__ import annotations

from sejoung.repositories.dependencies import get_user_repository
from sejoung.service.user_service import UserService


def get_user_service() -> UserService:
    return UserService(get_user_repository())
