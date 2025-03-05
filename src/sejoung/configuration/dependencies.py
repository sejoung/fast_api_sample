
def get_user_repository():
    from sejoung.repositories.user_repository import UserRepository
    return UserRepository(get_database().get_session)


def get_user_service():
    from sejoung.service.user_service import UserService

    return UserService(get_user_repository())


def get_database():
    from sejoung.configuration import Database
    _database = Database("mysql+aiomysql://root:root@localhost:3306/test")
    return _database
