from dependency_injector import providers, containers

from app.internal.repositories.postgres import (
    employees,
)

__all__ = ["PostgresContainer"]


class PostgresContainer(containers.DeclarativeContainer):
    employees = providers.Factory(employees.Employees)
