from app.database.crud import _create_uuid


def test_create_uuid():
    prefix = "test"
    result = _create_uuid(prefix)
    assert prefix in result
    assert len(result) == 14
