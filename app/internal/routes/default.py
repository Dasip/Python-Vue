from aiohttp import web
from dependency_injector.wiring import inject, Provide

from app.internal.pkg.models import Route
from app.internal.repositories import RepositoryContainer
from app.internal.repositories.postgres import PostgresContainer


__all__ = ["DefaultRoute"]

from app.internal.repositories.postgres.employees import Employees


class DefaultRoute(Route):
    __route_name = "/"

    @staticmethod
    @inject
    async def privet(
            request,
            repo: Employees = Provide[PostgresContainer.employees]):
        print(await repo.read_all_hierarchy())
        return web.Response(text="Privet")

    def get_route(self) -> web.RouteDef:
        return web.get(self.__route_name, self.privet)
