import logging
from typing import List, Optional, Dict, Any

import pydantic
from pydantic import ValidationError

from app.internal.repositories.postgres.employees import Employees
from app.pkg.models.exceptions.repository import EmptyResult, DriverError
from app.pkg.models.pydantic.employees import EmployeeHierarch, EmployeeCreateRequest, EmployeeUpdateRequest

__all__ = ["Employer"]


class Employer:
    __employees_repo: Employees

    def __init__(
        self,
        employees_repo: Employees
    ) -> None:
        self.__employees_repo = employees_repo

    async def read_hierarchy(self) -> List[EmployeeHierarch]:
        try:
            data = list(map(lambda x: x.to_dict(), await self.__employees_repo.read_all_hierarchy()))
            return sorted(data, key=lambda x: len(x.get("full_leader")))
        except EmptyResult:
            return []

    async def create_employee(self, data: Dict[Any, Any]) -> int:
        try:
            model = pydantic.parse_obj_as(EmployeeCreateRequest, data)
            await self.__employees_repo.create(model)
            return 200
        except DriverError:
            return 404
        except ValidationError as e:
            return 422

    async def update_employee(self, data: Dict[Any, Any]) -> int:
        try:
            model = pydantic.parse_obj_as(EmployeeUpdateRequest, data)
            await self.__employees_repo.update(model)
            return 200
        except DriverError:
            return 404
        except ValidationError as e:
            return 422
