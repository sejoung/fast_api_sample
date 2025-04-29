from dependency_injector import containers, providers

from sejoung.controller import UserController
from sejoung.repositories import UserRepository
from sejoung.service import UserService
from .database import AsyncDatabase
from .logger import create_logger


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        packages=["sejoung"]
    )

    logger = providers.Singleton(create_logger, name="sejoung")
    database = providers.Singleton(AsyncDatabase, logger=logger)
    user_repository: UserRepository = providers.Factory(UserRepository, session_factory=database.provided.session,
                                                        logger=logger)
    user_service: UserService = providers.Factory(UserService, user_repository=user_repository, logger=logger)
    user_controller: UserController = providers.Factory(UserController, user_service=user_service, logger=logger)
