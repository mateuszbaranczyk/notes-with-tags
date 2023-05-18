from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from app.database import crud
from app.database.db_config import Base, get_db
from app.database.db_models import Image, ImageWrite, Note, NoteWrite
from app.main import app
from app import api_models

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


def test_create_note():
    note_data = {"title": "title", "content": "content", "tags": ["tag1", "tag2"]}
    
    result = crud.create_note(db=Session(), note=api_models.Note(**note_data))
    assert result.title == note_data["title"]
