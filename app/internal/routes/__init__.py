from app.internal.pkg.models import RoutePackage
from app.internal.routes.default import DefaultRoute

__all__ = ["__routes__"]

__routes__ = RoutePackage(
    [
        DefaultRoute(),
    ]
).get_routes()
