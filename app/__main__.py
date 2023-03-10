from aiohttp import web
from app.configuration import __containers__
from app.configuration.server import Server
import asyncio
import sys


def get_app() -> web.Application:
    if sys.version_info >= (3, 8) and sys.platform.lower().startswith("win"):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    app = Server(web.Application()).get_app()
    __containers__.wire_packages(app=app)
    return app


if __name__ == "__main__":
    web.run_app(get_app())
