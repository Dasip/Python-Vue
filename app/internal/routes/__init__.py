from app.internal.pkg.models import RoutePackage
from app.internal.routes.employees_all import AllRoute
from app.internal.routes.employees_create import NewRoute

__all__ = ["__routes__"]

__routes__ = RoutePackage(
    [
        AllRoute(),
        NewRoute(),
    ]
).get_routes()
