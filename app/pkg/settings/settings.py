from functools import lru_cache
from pathlib import Path

import pydantic
from dotenv import find_dotenv
from pydantic import BaseSettings, SecretStr, PositiveInt, AnyUrl

__all__ = ["get_settings"]


class _Settings(BaseSettings):
    class Config:
        env_file_encoding = "utf-8"
        arbitrary_types_allowed = True
        case_sensitive = True


class Settings(_Settings):
    API_PORT: PositiveInt

    POSTGRES_USER: str
    POSTGRES_PASSWORD: SecretStr
    POSTGRES_HOST: str
    POSTGRES_PORT: PositiveInt
    POSTGRES_DATABASE: str


@lru_cache
def get_settings(env_file: str = ".env"):
    return Settings(_env_file=find_dotenv(env_file))
