import string

import shortuuid
from sqlalchemy.orm import Session

from app import api_models
from app.database import db_tables


def create_note(db: Session, note: api_models.NoteIn) -> api_models.Note:
    db_note = db_tables.Note(
        title=note.title,
        content=note.content,
        tags=note.tags,
        image=note.image,
        uuid=create_uuid(prefix="no"),
    )
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note


def create_image():
    pass


def read_note():
    pass


def read_image():
    pass


def create_uuid(prefix: str) -> str:
    alphabet = string.ascii_lowercase + string.digits
    suuid = shortuuid.ShortUUID(alphabet=alphabet)
    return f"{prefix}-{suuid.random(length=4)}-{suuid.random(length=4)}"
