import json

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200


def test_create_note():
    data = {"title": "title", "content": "test note", "tags": ["tag1", "tag2"], "image": None}
    response = client.put("/create_note/", json=data)
    response_body = json.loads(response.content)
    assert response.status_code == 200
    assert response_body == data


def test_create_note_with_img():
    data = {
        "title": "title",
        "content": "test note",
        "tags": ["tag1", "tag2"],
        "image": {"title": "photo_title", "url": "https://test.pl"},
    }
    response = client.put("/create_note/", json=data)
    response_body = json.loads(response.content)
    assert response.status_code == 200
    assert response_body == data


def test_get_note():
    title = "title"
    response = client.get(f"/note/{title}")
    assert response.status_code == 200
    assert response.content == {"title": "title"}
