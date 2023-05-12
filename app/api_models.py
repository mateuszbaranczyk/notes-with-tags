from pydantic import BaseModel, HttpUrl


class Image(BaseModel):
    title: str
    url: HttpUrl


class ImageOut(Image):
    uuid: str | None


class Note(BaseModel):
    title: str
    content: str
    tags: list[str]
    image: ImageOut | None


class NoteOut(Note):
    uuid: str | None
