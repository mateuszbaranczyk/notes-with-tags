import json
import random
from unittest.mock import ANY

from fastapi.testclient import TestClient
from requests import Response
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.api_models import UUID
from app.database.db_config import Base, get_db
from app.main import app

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200


def test_create_note():
    data = {"title": fake_title(), "content": "test note", "tags": "tag", "image": None}
    response = client.put("/create_note/", json=data)
    result = {"msg": "Created note!", "uuid": ANY, "image": None}
    assert_response(expected_result=result, response=response, status_code=200)


def test_create_note_with_img():
    image_data, image_uuid = create_image()
    image_data["uuid"] = image_uuid
    data = {
        "title": fake_title(),
        "content": "test note",
        "tags": "tag1",
        "image": image_uuid,
    }
    result = {"msg": "Created note!", "uuid": ANY, "image": image_uuid}
    response = client.put("/create_note/", json=data)
    assert_response(expected_result=result, response=response, status_code=200)


def test_get_note():
    note_title = create_note()
    result = {
        "title": note_title,
        "content": "note_content",
        "tags": "test_1",
        "uuid": ANY,
        "image": None,
    }
    response = client.get(f"/note/{note_title}")
    assert_response(expected_result=result, response=response, status_code=200)


def test_get_note_with_img():
    note_title, image_data = create_note(with_image=True)
    result = {
        "title": note_title,
        "content": "note_content",
        "tags": "test_1",
        "uuid": ANY,
        "image": image_data,
    }
    response = client.get(f"/note/{note_title}")
    assert_response(expected_result=result, response=response, status_code=200)


def test_get_tags():
    create_note()
    response = client.get("/tags/")
    assert response.status_code == 200


def test_add_image():
    data = {"title": "image", "url": "https://test.pl"}
    result = {"msg": "Image added!", "uuid": ANY}
    response = client.put("/add_image", json=data)
    assert_response(expected_result=result, status_code=200, response=response)


def test_get_image():
    image_data, image_uuid = create_image()
    response = client.get(f"/get_image/{image_uuid}")
    image_data["uuid"] = image_uuid
    assert_response(expected_result=image_data, response=response, status_code=200)


def assert_response(expected_result: dict, response: Response, status_code: int):
    response_body = json.loads(response.content)
    assert response.status_code == status_code
    assert response_body == expected_result


def create_image() -> tuple[dict, UUID]:
    data = {"title": "image", "url": "https://test.pl"}
    image = client.put("/add_image", json=data)
    image_uuid = json.loads(image.content)["uuid"]
    return data, image_uuid


def fake_title() -> str:
    return "".join((random.choice("abcdxyzpqr") for _ in range(5)))


def create_note(with_image: bool = False) -> tuple[str, str] | str:
    image_data, image_uuid = create_image()
    image_data["uuid"] = image_uuid
    note_data = {
        "title": fake_title(),
        "content": "note_content",
        "tags": "test_1",
        "image": image_uuid if with_image else None,
    }
    client.put("/create_note/", json=note_data)

    if with_image:
        return note_data["title"], image_data
    else:
        return note_data["title"]
