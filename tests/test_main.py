import json

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
    data = {
        "title": "title",
        "content": "test note",
        "tags": "tag",
    }
    response = client.put("/create_note/", json=data)
    assert response.status_code == 200
    assert response.json()["msg"] == "Created note!"


def _assert_response(expected_result: dict, response: Response, status_code: int):
    response_body = json.loads(response.content)
    assert response.status_code == status_code
    assert response_body == expected_result


# def test_create_note_with_img():
#     data = {
#         "title": "title",
#         "content": "test note",
#         "tags": "tag1",
#         "image": {"title": "photo_title", "url": "https://test.pl"},
#     }
#     response = client.put("/create_note/", json=data)
#     data["uuid"] = None
#     data["image"]["uuid"] = None
#     _assert_response(expected_result=data, response=response, status_code=200)


def test_get_note():
    result = {
        "title": "note_1",
        "content": "note_content",
        "tags": "test_1",
        "uuid": "no-test-test",
    }
    response = client.get(f"/note/{result['title']}")
    _assert_response(expected_result=result, response=response, status_code=200)


def test_get_tags():
    result = ["tag1", "tag2"]
    response = client.get("/tags/")
    response_body = json.loads(response.text)
    response_body.sort()
    assert result == response_body
