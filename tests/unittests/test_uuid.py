from app.database.crud import create_uuid


def test_create_uuid():
    prefix = "test"
    result = create_uuid(prefix)
    assert prefix in result
    assert len(result) == 14
