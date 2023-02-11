from aiohttp import web

from app.internal.pkg.models import Route

__all__ = ["DefaultRoute"]


class DefaultRoute(Route):
    __route_name = "/"

    @staticmethod
    async def privet(request):
        return web.Response(text="Privet")

    def get_route(self) -> web.RouteDef:
        return web.get(self.__route_name, self.privet)
