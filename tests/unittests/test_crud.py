from app.database import crud

from app.database.db_models import ImageWrite, ImageRead, NoteRead, NoteWrite

def test_create_note():
    note_data = {}
    result = crud.create_note()
    assert result.title == note_data["title"]
    
