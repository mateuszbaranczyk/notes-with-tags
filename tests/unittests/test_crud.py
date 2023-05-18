from app.database import crud
from app.database.db_models import ImageRead, ImageWrite, NoteRead, NoteWrite


def test_create_note():
    note_data = {"title": "title", "content": "content", "tags": ["tag1", "tag2"]}
    result = crud.create_note()
    assert result.title == note_data["title"]
