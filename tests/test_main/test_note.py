from unittest.mock import ANY

from tests.utils import assert_response, create_image, create_note, fake_title


def test_create_note(client):
    data = {"title": fake_title(), "content": "test note", "tags": "tag", "image": None}
    response = client.put("/create_note/", json=data)
    result = {"msg": "Created note!", "uuid": ANY, "image": None}
    assert_response(expected_result=result, response=response)


def test_create_note_with_img(client):
    image_data, image_uuid = create_image(client)
    image_data["uuid"] = image_uuid
    data = {
        "title": fake_title(),
        "content": "test note",
        "tags": "tag1",
        "image": image_uuid,
    }
    result = {"msg": "Created note!", "uuid": ANY, "image": image_uuid}
    response = client.put("/create_note/", json=data)
    assert_response(expected_result=result, response=response)


def test_get_note(client):
    note_title = create_note(client)
    result = {
        "title": note_title,
        "content": "note_content",
        "tags": "test_1",
        "uuid": ANY,
        "image": None,
    }
    response = client.get(f"/note/{note_title}")
    assert_response(expected_result=result, response=response)


def test_get_note_with_img(client):
    note_title, image_data = create_note(client=client, with_image=True)
    result = {
        "title": note_title,
        "content": "note_content",
        "tags": "test_1",
        "uuid": ANY,
        "image": image_data,
    }
    response = client.get(f"/note/{note_title}")
    assert_response(expected_result=result, response=response)
