import json

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200


def test_create_note():
    data = {"text": "test note", "tags": ["tag1", "tag2"], "image": None}
    response = client.put("/create_note/", json=data)
    response_body = json.loads(response.text)
    assert response.status_code == 200
    assert response_body == data


def test_create_note_with_img():
    data = {
        "text": "test note",
        "tags": ["tag1", "tag2"],
        "image": {"title": "photo_title", "url": "https://test.pl"},
    }
    response = client.put("/create_note/", json=data)
    response_body = json.loads(response.text)
    assert response.status_code == 200
    assert response_body == data