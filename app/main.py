from fastapi import Depends, FastAPI

from app import api_models
from app.api_models import UUID
from app.database import crud
from app.database.db_config import get_db, prepare_database

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    prepare_database()


@app.get("/")
async def root():
    return {"msg": "Hello World"}


@app.put("/create_note/", response_model=dict)
async def create_note(note: api_models.NoteIn, db=Depends(get_db)):
    db_note = crud.create_note(db, note)
    return {"msg": "Created note!", "uuid": db_note.uuid, "image": db_note.image_uuid}


@app.get("/note/{title}", response_model=api_models.Note)
async def get_note(title: str, db=Depends(get_db)):
    note = crud.get_note(db, title)
    return note


@app.put("/add_image/", response_model=dict)
async def add_image(image: api_models.ImageIn, db=Depends(get_db)):
    db_image = crud.add_image(db, image)
    return {"msg": "Image added!", "uuid": db_image.uuid}


@app.get("/get_image/{uuid}", response_model=api_models.Image)
async def get_image(uuid: UUID, db=Depends(get_db)):
    image = crud.get_image(db, uuid)
    return image


@app.get("/tags/", response_model=set[str])
async def get_tags(db=Depends(get_db)):
    tags = crud.get_tags(db)
    return tags
