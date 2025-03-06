from sejoung.configuration import get_database
from .user_repository import UserRepository


def get_user_repository() -> UserRepository:
    database = get_database()
    return UserRepository(database.get_session)
