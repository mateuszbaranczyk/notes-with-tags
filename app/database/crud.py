from app.database import db_models
from sqlalchemy.orm import Session
from app import api_models


def create_note(db: Session, note: api_models.Note) -> db_models.Note:
    db_note = db_models.NoteWrite(
        title=note.title, content=note.content, tags=note.tags, image=note.image
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
