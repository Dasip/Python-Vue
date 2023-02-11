from aiohttp import web
from app.internal.routes import __routes__

__all__ = ["Server"]


class Server:

    __app: web.Application

    def __init__(self, app: web.Application) -> None:
        self.__app = app
        self.connect_routes()

    def connect_routes(self) -> None:
        self.__app.add_routes(__routes__)

    def get_app(self) -> web.Application:
        return self.__app
