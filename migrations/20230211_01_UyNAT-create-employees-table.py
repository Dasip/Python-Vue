"""
Create employees table
"""

from yoyo import step

__depends__ = {}

steps = [
    step("""
        create table if not exists employees (
            id serial not null primary key,
            full_name varchar(150) not null,
            position varchar(150) not null,
            salary bigint not null,
            start_date timestamp not null,
            leader int,
            foreign key (leader) references employees(leader)
        );
    """,
         "drop table if exists employees;")
]
