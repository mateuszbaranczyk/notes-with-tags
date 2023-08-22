from app.database.crud import create_note
from app.api_models import NoteIn


def test_create_note(session):
    note = NoteIn(title="test titie", content="test content", tags="test tag")
    result = create_note(session, note)
    assert result
