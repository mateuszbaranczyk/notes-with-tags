from pydantic import BaseModel, HttpUrl


class Image(BaseModel):
    title: str
    url: HttpUrl


class Note(BaseModel):
    title: str
    content: str
    tags: list[str]
    image: Image | None

