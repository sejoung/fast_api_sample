from sejoung.configuration import get_database
from .user_repository import UserRepository


def get_user_repository() -> UserRepository:
    return UserRepository(get_database().get_session)
