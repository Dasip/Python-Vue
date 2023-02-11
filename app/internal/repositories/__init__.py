from dependency_injector import containers, providers

from app.internal.repositories.postgres import PostgresContainer

__all__ = ["RepositoryContainer", "PostgresContainer"]


class RepositoryContainer(containers.DeclarativeContainer):
    postgres = providers.Container(PostgresContainer)
