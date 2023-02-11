from dependency_injector import containers, providers
from app.pkg.connectors.postgres import Postgres
from app.pkg.settings import settings

__all__ = ["Connectors", "Postgres"]


class Connectors(containers.DeclarativeContainer):

    config = providers.Configuration(name="settings", pydantic_settings=[settings])

    postgresql = providers.Singleton(
        Postgres,
        username=config.POSTGRES_USER,
        password=config.POSTGRES_PASSWORD,
        host=config.POSTGRES_HOST,
        port=config.POSTGRES_PORT,
        database_name=config.POSTGRES_DATABASE,
    )
