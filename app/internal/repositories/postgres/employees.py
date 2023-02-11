from typing import List
from app.internal.repositories.postgres.handlers.collect_response import (
    collect_response,
)
from app.internal.repositories.repository import Repository
from app.internal.repositories.postgres.connection import get_connection
from app.pkg.models.base import Model
from app.pkg.models.pydantic.employees import Employee, EmployeeCreateRequest, EmployeeHierarch, EmployeeUpdateRequest

__all__ = ["Employees"]


class Employees(Repository):

    @collect_response
    async def create(self, cmd: EmployeeCreateRequest) -> Employee:
        q = """
        insert into employees
            (
                full_name,
                position,
                salary,
                start_date,
                leader
            )
        values
            (
                %(full_name)s,
                %(position)s,
                %(salary)s,
                %(start_date)s,
                %(leader_id)s
            )
        returning
            id,
            full_name,
            position,
            salary,
            start_date
            ;
        """
        async with get_connection() as cur:
            await cur.execute(q, cmd.to_dict())
            return await cur.fetchone()

    @collect_response
    async def read(self) -> Model:
        raise NotImplementedError

    @collect_response
    async def read_all(self) -> List[Employee]:
        q = """
        select * from employees;
        """
        async with get_connection() as cur:
            await cur.execute(q)
            return await cur.fetchall()

    @collect_response
    async def read_all_hierarchy(self) -> List[EmployeeHierarch]:
        q = """
        with recursive hierarchy_table as (

            select
                id,
                full_name,
                position,
                salary,
                start_date,
                '' as full_leader
            from employees
            where
                leader is null
            
            union all
            
            select
                employ.id,
                employ.full_name,
                employ.position,
                employ.salary,
                employ.start_date,
                hierarchy_table.full_leader || '_' || employ.leader
            from
                employees employ,
                hierarchy_table
            where
                employ.leader = hierarchy_table.id
        )
        select
            id,
            full_name,
            position,
            salary,
            start_date,
            full_leader
        from
            hierarchy_table;
        """
        async with get_connection() as cur:
            await cur.execute(q)
            return await cur.fetchall()

    @collect_response
    async def update(self, cmd: EmployeeUpdateRequest) -> Employee:
        q = """
        update employees
        set
            full_name = %(full_name)s,
            position = %(position)s,
            salary = %(salary)s,
            start_date = %(start_date)s,
            leader = %(leader_id)s
        where id = %(id)s
        returning
            id,
            full_name,
            position,
            salary,
            start_date,
            leader;
        """
        async with get_connection() as cur:
            await cur.execute(q, cmd.to_dict())
            return await cur.fetchone()

    @collect_response
    async def delete(self, cmd: Model) -> Model:
        raise NotImplementedError
