from dependency_injector import containers, providers

from sejoung.configuration import Database
from sejoung.controller import UserController
from sejoung.repositories import UserRepository
from sejoung.service import UserService


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        packages=["sejoung"]
    )
    database = providers.Singleton(Database)
    user_repository: UserRepository = providers.Factory(UserRepository, database.provided.session)
    user_service: UserService = providers.Factory(UserService, user_repository=user_repository)
    user_controller: UserController = providers.Factory(UserController, user_service=user_service)
