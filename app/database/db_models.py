import string
from typing import List

import shortuuid
from sqlalchemy import Column, String, Text
from sqlalchemy.orm import relationship

from app.database import db_config


class Image(db_config.Base):
    __tablename__ = "images"

    uuid = Column(String, primary_key=True, index=True)
    title = Column(String, index=True)
    url = Column(String)


class Note(db_config.Base):
    __tablename__ = "notes"

    uuid = Column(String, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(Text)
    tags = Column(List)
    image = relationship("Image", back_populates="owner")


def create_uuid(prefix: str) -> str:
    alphabet = string.ascii_lowercase + string.digits
    suuid = shortuuid.ShortUUID(alphabet=alphabet)
    return f"{prefix}-{suuid.random(length=4)}-{suuid.random(length=4)}"
