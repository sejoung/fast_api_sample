from dependency_injector import containers, providers

from sejoung.configuration.database import Database
from sejoung.controller import UserController
from sejoung.repositories.user import UserRepository


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=["sejoung"])


    database = providers.Singleton(Database, db_url="mysql://root:root@localhost:3306/test")

    user_repository = providers.Factory(
        UserRepository,
        session=database.provided.get_session,
    )

    user_controller = providers.Factory(UserController, user_repository=user_repository.provided)


