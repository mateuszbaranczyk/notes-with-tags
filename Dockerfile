FROM python:3.10-slim

RUN pip install "poetry==1.4.2"
WORKDIR /code

COPY poetry.lock pyproject.toml /code/
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

COPY . /code

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]