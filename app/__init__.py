from aiohttp import web

from app.configuration.server import Server


def get_app():
    return Server(web.Application()).get_app()
