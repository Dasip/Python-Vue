from aiopg.connection import Cursor
from contextlib import asynccontextmanager
from dependency_injector.wiring import Provide, inject
from psycopg2.extras import RealDictCursor
from app.pkg.connectors import Connectors, Postgres


@asynccontextmanager
@inject
async def get_connection(
    postgres: Postgres = Provide[Connectors.postgresql],
) -> Cursor:
    async with postgres.get_connect() as connection:
        async with (await connection.cursor(cursor_factory=RealDictCursor)) as cur:
            yield cur
