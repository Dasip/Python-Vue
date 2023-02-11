FROM python:3.9.5

RUN apt-get update && \
    apt-get install -y --no-install-recommends dos2unix

WORKDIR /migration_on
COPY ./ /migration_on/
COPY ./app /migration_on/app
COPY ./migrations /migration_on/migrations
COPY ./scripts /migration_on/scripts
COPY ./scripts/migrate.py /migration_on/migrate.py

RUN chmod +x scripts/wait-for-server.sh
RUN dos2unix scripts/*

RUN pip install poetry
RUN poetry install --no-dev
RUN poetry config virtualenvs.create false
