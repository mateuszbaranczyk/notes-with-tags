import json

from fastapi.testclient import TestClient
from requests import Response

from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200


def test_create_note():
    data = {
        "title": "title",
        "content": "test note",
        "tags": ["tag1", "tag2"],
        "image": None,
    }
    response = client.put("/create_note/", json=data)
    data["uuid"] = None
    _assert_response(expected_result=data, response=response, status_code=200)


def _assert_response(expected_result: dict, response: Response, status_code: int):
    response_body = json.loads(response.content)
    assert response.status_code == status_code
    assert response_body == expected_result


def test_create_note_with_img():
    data = {
        "title": "title",
        "content": "test note",
        "tags": ["tag1", "tag2"],
        "image": {"title": "photo_title", "url": "https://test.pl"},
    }
    response = client.put("/create_note/", json=data)
    data["uuid"] = None
    data["image"]["uuid"] = None
    _assert_response(expected_result=data, response=response, status_code=200)


def test_get_note():
    result = {
        "title": "note_1",
        "content": "note_content",
        "tags": ["test_1", "test_2"],
        "image": None,
    }
    response = client.get(f"/note/{result['title']}")
    result["uuid"] = None
    _assert_response(expected_result=result, response=response, status_code=200)


def test_get_tags():
    result = ["tag1", "tag2"]
    response = client.get("/tags/")
    response_body = json.loads(response.text)
    response_body.sort()
    assert result == response_body
