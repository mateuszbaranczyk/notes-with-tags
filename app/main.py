from typing import Annotated

from fastapi import Body, Depends, FastAPI

from app import api_models
from app.database import crud
from app.database.db_config import get_db, prepare_database

app = FastAPI()


database_result = {"title": "note_1", "content": "note_content", "tags": "test_1", "uuid": "no-test-test"}
tags_from_db = ["tag1", "tag2", "tag2"]


@app.on_event("startup")
async def startup_event():
    prepare_database()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.put("/create_note/")
async def create_note(note: api_models.NoteIn, db=Depends(get_db)):
    crud.create_note(db, note)
    return {"msg": "Created note!"}


@app.get("/note/{title}", response_model=api_models.Note)
async def get_note(title: str):
    return database_result


@app.get("/tags/")
async def get_tags() -> set[str]:
    tags = set(tags_from_db)
    return tags
