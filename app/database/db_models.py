import string
from typing import NewType

import shortuuid
from pydantic import BaseModel, HttpUrl

UUID = NewType("UUID", str)


def create_uuid(prefix: str) -> str:
    alphabet = string.ascii_lowercase + string.digits
    suuid = shortuuid.ShortUUID(alphabet=alphabet)
    return f"{prefix}-{suuid.random(length=4)}-{suuid.random(length=4)}"


class ImageBase(BaseModel):
    title: str
    url: HttpUrl


class ImageWrite(ImageBase):
    uuid: UUID = create_uuid(prefix="ig")


class Image(ImageBase):
    uuid: UUID

    class Config:
        orm_mode = True


class NoteBase(BaseModel):
    title: str
    content: str
    tags: list[str]
    image: Image | None


class NoteWrite(NoteBase):
    uuid: UUID = create_uuid(prefix="no")


class Note(NoteBase):
    uuid: UUID

    class Config:
        orm_mode = True
