from contextlib import asynccontextmanager
from typing import Optional
import aiopg
from aiopg import Connection
from pydantic import SecretStr, PositiveInt
from app.pkg.connectors.base_connector import BaseConnector

__all__ = ["Postgres"]


class Postgres(BaseConnector):

    __username: str
    __password: SecretStr
    __host: str
    __port: PositiveInt
    __database_name: str
    __pool: Optional[aiopg.Pool]

    def __init__(
        self,
        username: str,
        password: SecretStr,
        host: str,
        port: PositiveInt,
        database_name: str,
    ) -> None:
        self.__username = username
        self.__password = password
        self.__host = host
        self.__port = port
        self.__database_name = database_name
        self.__pool = None

    def get_dsn(self) -> str:
        return (
            f"postgres://"
            f"{self.__username}:{self.__password.get_secret_value()}@"
            f"{self.__host}:{self.__port}/"
            f"{self.__database_name}"
        )

    @asynccontextmanager
    async def get_connect(self) -> Connection:
        if self.__pool is None:
            self.__pool = await aiopg.create_pool(dsn=self.get_dsn())

        async with self.__pool.acquire() as conn:
            yield conn
