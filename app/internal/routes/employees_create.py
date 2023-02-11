from aiohttp import web
from dependency_injector.wiring import inject, Provide
from app.internal.pkg.models import Route
from app.internal.services import Employer, Services


__all__ = ["NewRoute"]


class NewRoute(Route):
    __route_name = "/employees/new"

    @staticmethod
    @inject
    async def create_one(
            request: web.Request,
            service: Employer = Provide[Services.employer_service]
    ):
        new_data = await service.create_employee(await request.json())
        return web.json_response(new_data, content_type="application/json", status=200)

    def get_route(self) -> web.RouteDef:
        return web.post(self.__route_name, self.create_one)
