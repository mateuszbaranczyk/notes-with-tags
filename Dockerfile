FROM python:3.10

WORKDIR /code

COPY ./poetry.lock ./pyproject.toml /code/

RUN pip install poetry
RUN poetry install

COPY ./app /code/app


EXPOSE 8000

CMD "uvicorn code.app.main:app"