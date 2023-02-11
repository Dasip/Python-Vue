import datetime
from typing import List

import pydantic
from pydantic import validator, ValidationError

from app.pkg.models.base import BaseModel

__all__ = ["Employee", "EmployeeCreateRequest", "EmployeeHierarch"]


class BaseEmployee(BaseModel):
    """Base pair model"""


class Employee(BaseEmployee):
    id: int
    full_name: str
    position: str
    start_date: datetime.datetime
    salary: pydantic.PositiveInt


class EmployeeHierarch(BaseEmployee):
    id: int
    full_name: str
    position: str
    start_date: datetime.datetime
    salary: pydantic.PositiveInt
    full_leader: List[int]

    @validator("full_leader", pre=True)
    def sql_recursive_conversion(cls, value):
        if type(value) is str:
            if value == "":
                return []

            new_list = value[1:].split("_")
            return list(map(int, new_list))

        raise ValidationError


class EmployeeCreateRequest(BaseEmployee):
    full_name: str
    position: str
    start_date: datetime.datetime
    salary: pydantic.PositiveInt
