from tests.utils import create_note


def test_get_tags(client):
    create_note(client)
    response = client.get("/tags/")
    assert response.status_code == 200
