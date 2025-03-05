from sejoung.repositories import get_user_repository
from .user_service import UserService


def get_user_service() -> UserService:
    return UserService(get_user_repository())
