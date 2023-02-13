FROM python:3.9.5

WORKDIR /usr/src/app
COPY ./ /usr/src/app

RUN rm frontend -r

RUN pip install poetry
RUN poetry install --only main