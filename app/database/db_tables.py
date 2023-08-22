from sqlalchemy import Column, ForeignKey, String, Text
from sqlalchemy.orm import relationship

from app.database import db_config


class Image(db_config.Base):
    __tablename__ = "images"

    uuid = Column(String, primary_key=True, index=True, unique=True)
    title = Column(String, index=True)
    url = Column(String)


class Note(db_config.Base):
    __tablename__ = "notes"

    uuid = Column(String, primary_key=True, index=True, unique=True)
    title = Column(String, index=True)
    content = Column(Text)

    tags = relationship("Tag", secondary="note_tags", back_populates="notes")

    image_uuid = Column(String, ForeignKey("images.uuid"))
    image = relationship("Image")


class Tag(db_config.Base):
    __tablename__ = "tags"

    uuid = Column(String, primary_key=True, index=True, unique=True)
    title = Column(String, index=True, unique=True)

    notes = relationship("Note", secondary="note_tags", back_populates="tags")
