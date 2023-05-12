FROM python:3.10 as requirements-stage
WORKDIR /tmp
RUN pip install poetry
COPY ./pyproject.toml ./poetry.lock* /tmp/
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.10
WORKDIR /code
COPY --from=requirements-stage /tmp/requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app
EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

# FROM python:3.10-slim

# RUN pip install "poetry==1.4.2"
# WORKDIR /code

# COPY poetry.lock pyproject.toml /code/
# RUN poetry config virtualenvs.create false && \
#     poetry install --no-interaction --no-ansi

# COPY chat/ /code

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]