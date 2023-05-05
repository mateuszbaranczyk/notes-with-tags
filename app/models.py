from enum import Enum

from pydantic import BaseModel, Field, HttpUrl


class Image(BaseModel):
    title: str
    url: HttpUrl


class Note(BaseModel):
    content: str
    tags: list[str]
    image: Image | None

