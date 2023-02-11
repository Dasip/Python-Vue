from aiohttp import web
from dependency_injector.wiring import inject, Provide
from app.internal.pkg.models import Route
from app.internal.services import Employer, Services


__all__ = ["AllRoute"]


class AllRoute(Route):
    __route_name = "/employees/all"

    @staticmethod
    @inject
    async def get_all(
            request: web.Request,
            service: Employer = Provide[Services.employer_service]
    ):
        new_data = await service.read_hierarchy()
        return web.json_response(new_data, content_type="application/json", status=200)

    def get_route(self) -> web.RouteDef:
        return web.get(self.__route_name, self.get_all)
