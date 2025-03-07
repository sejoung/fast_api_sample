from .user_repository import UserRepository
from ..configuration import Database


def get_user_repository() -> UserRepository:
    return UserRepository(Database.get_instance().get_session)
