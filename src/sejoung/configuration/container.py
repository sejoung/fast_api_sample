from dependency_injector import containers, providers

from sejoung.configuration.database import Database
from sejoung.repositories.user import UserRepository


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=["sejoung.application"])

    config = providers.Configuration(yaml_files=["config.yml"])

    print("asdsad ", config.db.url)

    database = providers.Singleton(Database, db_url=config.db.url)

    user_repository = providers.Factory(
        UserRepository,
        session_factory=database.provided.session
    )
