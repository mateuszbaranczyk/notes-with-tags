import json
import random

from requests import Response

from app.api_models import UUID


def create_image(client) -> tuple[dict, UUID]:
    data = {"title": "image", "url": "https://test.pl"}
    image = client.put("/add_image", json=data)
    image_uuid = json.loads(image.content)["uuid"]
    return data, image_uuid


def fake_title() -> str:
    return "".join((random.choice("abcdxyzpqr") for _ in range(5)))


def create_note(client, with_image: bool = False) -> tuple[str, str] | str:
    image_data, image_uuid = create_image(client)
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


def assert_response(expected_result: dict, response: Response, status_code: int = 200):
    response_body = json.loads(response.content)
    assert response.status_code == status_code
    assert response_body == expected_result
