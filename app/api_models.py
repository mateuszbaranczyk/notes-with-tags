from typing import NewType

from pydantic import BaseModel, HttpUrl

UUID = NewType("UUID", str)


class ImageIn(BaseModel):
    title: str
    url: HttpUrl


class Image(ImageIn):
    uuid: UUID

    class Config:
        orm_mode = True


class NoteIn(BaseModel):
    title: str
    content: str
    tags: str
    # image: Image | None


class Note(NoteIn):
    uuid: UUID

    class Config:
        orm_mode = True
