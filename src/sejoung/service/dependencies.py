from .user_service import UserService
from ..repositories.dependencies import get_user_repository


def get_user_service() -> UserService:
    return UserService(get_user_repository())
