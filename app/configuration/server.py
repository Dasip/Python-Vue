from aiohttp import web
from app.internal.routes import __routes__
import aiohttp_cors

__all__ = ["Server"]


class Server:

    __app: web.Application

    def __init__(self, app: web.Application) -> None:
        self.__app = app
        self.connect_routes()
        self.enable_cors()

    def connect_routes(self) -> None:
        self.__app.add_routes(__routes__)

    def enable_cors(self) -> None:
        cors = aiohttp_cors.setup(
            self.__app,
            defaults={
                "*": aiohttp_cors.ResourceOptions(
                    allow_credentials=True,
                    expose_headers="*",
                    allow_headers="*"
                )
            }
        )

        for route in list(self.__app.router.routes()):
            cors.add(route)

    def get_app(self) -> web.Application:
        return self.__app
