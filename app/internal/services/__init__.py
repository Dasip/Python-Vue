from dependency_injector import containers, providers
from app.pkg.settings import settings
from app.internal.repositories import RepositoryContainer
from app.internal.services.employer import Employer

__all__ = [
    "Employer",
    "Services"
]


class Services(containers.DeclarativeContainer):

    config = providers.Configuration(name="settings", pydantic_settings=[settings])

    repos = providers.Container(RepositoryContainer)
    postgres = repos.postgres

    employer_service = providers.Factory(
        Employer,
        employees_repo=postgres.employees,
    )
