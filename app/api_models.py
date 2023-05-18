from pydantic import BaseModel, HttpUrl


class ImageIn(BaseModel):
    title: str
    url: HttpUrl


class Image(ImageIn):
    uuid: str | None


class NoteIn(BaseModel):
    title: str
    content: str
    tags: list[str]
    image: Image | None


class Note(NoteIn):
    uuid: str | None
