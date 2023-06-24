from unittest.mock import ANY

from tests.utils import assert_response, create_image


def test_add_image(client):
    data = {"title": "image", "url": "https://test.pl"}
    result = {"msg": "Image added!", "uuid": ANY}
    response = client.put("/add_image", json=data)
    assert_response(expected_result=result, response=response)


def test_get_image(client):
    image_data, image_uuid = create_image(client)
    response = client.get(f"/get_image/{image_uuid}")
    image_data["uuid"] = image_uuid
    assert_response(expected_result=image_data, response=response)
