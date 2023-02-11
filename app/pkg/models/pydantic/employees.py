import datetime
from typing import List, Optional

import pydantic
from pydantic import validator, ValidationError

from app.pkg.models.base import BaseModel

__all__ = ["Employee", "EmployeeCreateRequest", "EmployeeHierarch", "EmployeeUpdateRequest"]


class BaseEmployee(BaseModel):
    """Base pair model"""


class Employee(BaseEmployee):
    id: int
    full_name: str
    position: str
    start_date: datetime.datetime
    salary: pydantic.PositiveInt
    leader: Optional[int]


class EmployeeHierarch(BaseEmployee):
    id: int
    full_name: str
    position: str
    start_date: str
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

    @validator("start_date", pre=True)
    def datetime_conversion(cls, value):
        if type(value) is str:
            return value

        if type(value) is datetime.datetime:
            return value.strftime("%d.%m.%Y")

        raise ValidationError


class EmployeeCreateRequest(BaseEmployee):
    full_name: str
    position: str
    start_date: datetime.datetime
    salary: pydantic.PositiveInt
    leader_id: Optional[int]

    @validator("start_date", pre=True)
    def datetime_conversion(cls, value):
        if type(value) is str:
            return datetime.datetime.strptime(value, "%d.%m.%Y")

        if type(value) is datetime.datetime:
            return value

        raise ValidationError


class EmployeeUpdateRequest(BaseEmployee):
    id: int
    full_name: str
    position: str
    start_date: datetime.datetime
    salary: pydantic.PositiveInt
    leader_id: Optional[int]

    @validator("start_date", pre=True)
    def datetime_conversion(cls, value):
        if type(value) is str:
            return datetime.datetime.strptime(value, "%d.%m.%Y")

        if type(value) is datetime.datetime:
            return value

        raise ValidationError
