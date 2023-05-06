import string

import shortuuid
from pydantic import BaseModel, HttpUrl


def create_uuid(prefix: str) -> str:
    alphabet = string.ascii_lowercase + string.digits
    suuid = shortuuid.ShortUUID(alphabet=alphabet)
    return f"{prefix}-{suuid.random(length=4)}-{suuid.random(length=4)}"


class Image(BaseModel):
    uuid: str = create_uuid(prefix="ig")
    title: str
    url: HttpUrl


class Note(BaseModel):
    uuid: str = create_uuid(prefix="no")
    title: str
    content: str
    tags: list[str]
    image: Image | None
