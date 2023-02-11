from dataclasses import dataclass, field
from typing import Callable, List, Optional

from dependency_injector import containers
from aiohttp import web

__all__ = ["Container", "Containers"]


@dataclass(frozen=True)
class Container:
    container: Callable[..., containers.Container]
    packages: List[str] = field(default_factory=lambda: ["app"])


@dataclass(frozen=True)
class Containers:
    pkg_name: str
    containers: List[Container]

    def wire_packages(
        self, app: Optional[web.Application] = None, pkg_name: Optional[str] = None
    ) -> None:
        pkg_name = pkg_name if pkg_name else self.pkg_name
        for container in self.containers:
            cont = container.container()
            cont.wire(packages=[pkg_name, *container.packages])
            if app:
                setattr(app, container.container.__name__.lower(), cont)
