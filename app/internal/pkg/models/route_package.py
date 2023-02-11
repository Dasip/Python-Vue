from typing import List

from aiohttp import web

from app.internal.pkg.models.route import Route

__all__ = ["RoutePackage"]


class RoutePackage:
    __routes: List[Route]

    def __init__(self, routes: List[Route]):
        self.__routes = routes

    def get_routes(self) -> List[web.RouteDef]:
        return list(map(lambda x: x.get_route(), self.__routes))
