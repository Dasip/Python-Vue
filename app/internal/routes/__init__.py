from app.internal.pkg.models import RoutePackage
from app.internal.routes.employees_all import AllRoute
from app.internal.routes.employees_create import NewRoute
from app.internal.routes.employees_update import UpdateRoute

__all__ = ["__routes__"]

__routes__ = RoutePackage(
    [
        AllRoute(),
        NewRoute(),
        UpdateRoute(),
    ]
).get_routes()
