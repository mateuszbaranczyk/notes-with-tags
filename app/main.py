from fastapi import Depends, FastAPI

from app import api_models
from app.api_models import UUID
from app.database import crud
from app.database.db_config import get_db, prepare_database

app = FastAPI()


database_result = {
    "title": "note_1",
    "content": "note_content",
    "tags": "test_1",
    "uuid": "no-test-test",
}
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


@app.put("/add_image/")
async def add_image(image: api_models.ImageIn, db=Depends(get_db)):
    created_object = crud.add_image(db, image)
    return {"msg": "Image added!", "uuid": created_object.uuid}


@app.get("/get_image/{uuid}", response_model=api_models.Image)
async def get_image(uuid: UUID, db=Depends(get_db)):
    image = crud.get_image(db, uuid)
    return image


@app.get("/tags/")
async def get_tags() -> set[str]:
    tags = set(tags_from_db)
    return tags
