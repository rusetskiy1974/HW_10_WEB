FROM python:3.11

WORKDIR /app

COPY poetry.lock .

COPY pyproject.toml .

COPY hw10_project .

RUN pip install poetry

RUN poetry install

EXPOSE 8000


