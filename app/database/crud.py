import string

import shortuuid
from sqlalchemy.orm import Session

from app import api_models
from app.api_models import UUID
from app.database import db_tables


def create_note(db: Session, note: api_models.NoteIn) -> api_models.Note:
    db_note = db_tables.Note(
        title=note.title,
        content=note.content,
        tags=note.tags,
        # image=note.image,
        uuid=create_uuid(prefix="no"),
    )
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note


def get_note():
    pass


def add_image(db: Session, image: api_models.ImageIn) -> api_models.Image:
    db_image = db_tables.Image(
        title=image.title,
        url=image.url,
        uuid=create_uuid(prefix="ig"),
    )
    db.add(db_image)
    db.commit()
    db.refresh(db_image)
    return db_image


def get_image(db: Session, uuid: UUID) -> api_models.Image:
    return db.query(db_tables.Image).filter(db_tables.Image.uuid == uuid).first()


def create_uuid(prefix: str) -> UUID:
    alphabet = string.ascii_lowercase + string.digits
    suuid = shortuuid.ShortUUID(alphabet=alphabet)
    return f"{prefix}-{suuid.random(length=4)}-{suuid.random(length=4)}"
