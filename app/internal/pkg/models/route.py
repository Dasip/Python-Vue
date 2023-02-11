from abc import ABC
from aiohttp import web


__all__ = ["Route"]


class Route(ABC):
    __route_name: str

    def get_route(self) -> web.RouteDef:
        raise NotImplementedError
