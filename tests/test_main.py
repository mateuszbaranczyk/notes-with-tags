import json
from unittest.mock import ANY

from fastapi.testclient import TestClient
from requests import Response
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

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

# TODO replace response models by models from db_models


def test_root():
    response = client.get("/")
    assert response.status_code == 200


def test_create_note():
    data = {"title": "title", "content": "test note", "tags": "tag", "image": None}
    response = client.put("/create_note/", json=data)
    result = {"msg": "Created note!", "uuid": ANY}
    assert_response(expected_result=result, response=response, status_code=200)


def assert_response(expected_result: dict, response: Response, status_code: int):
    response_body = json.loads(response.content)
    assert response.status_code == status_code
    assert response_body == expected_result


def test_create_note_with_img():
    data = {
        "title": "title",
        "content": "test note",
        "tags": "tag1",
        "image": "ig-test-test",
    }
    result = {"msg": "Created note!", "uuid": ANY}
    response = client.put("/create_note/", json=data)
    assert_response(expected_result=result, response=response, status_code=200)


def test_get_note():
    result = {
        "title": "note_1",
        "content": "note_content",
        "tags": "test_1",
        "uuid": "no-test-test",
        "image": None,
    }
    response = client.get(f"/note/{result['title']}")
    assert_response(expected_result=result, response=response, status_code=200)


def test_get_tags():
    result = ["tag1", "tag2"]
    response = client.get("/tags/")
    response_body = json.loads(response.text)
    response_body.sort()
    assert result == response_body


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


def create_image():
    data = {"title": "image", "url": "https://test.pl"}
    image = client.put("/add_image", json=data)
    image_uuid = json.loads(image.content)["uuid"]
    return data, image_uuid
