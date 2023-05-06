import string
import shortuuid


def create_uuid(prefix: str) -> str:
    alphabet = string.ascii_lowercase + string.digits
    suuid = shortuuid.ShortUUID(alphabet=alphabet)
    return f"{prefix}-{suuid.random(length=4)}-{suuid.random(length=4)}"


def test_create_uuid():
    prefix = "test"
    result = create_uuid(prefix)
    assert prefix in result
    assert len(result) == 14
