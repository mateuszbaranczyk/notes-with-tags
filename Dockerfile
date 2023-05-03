FROM python:3.10

WORKDIR /code

COPY ./poetry.lock ./pyproject.toml /code/

RUN pip install poetry
    poetry install

COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]