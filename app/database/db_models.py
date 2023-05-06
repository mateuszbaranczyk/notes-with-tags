from typing import List

from sqlalchemy import Column, String, Text
from sqlalchemy.orm import relationship

from app.database import db_config


class UUID:
    def __init__(self) -> None:
        pass


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