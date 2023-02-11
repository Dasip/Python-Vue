from app.configuration.server import Server
from app.pkg.models.core import Containers, Container
from app.pkg.connectors import Connectors
from app.internal.repositories import PostgresContainer

__all__ = ["Server", "__containers__"]


__containers__ = Containers(
    pkg_name=__name__,
    containers=[
        Container(container=Connectors),
        Container(container=PostgresContainer),
    ]
)
