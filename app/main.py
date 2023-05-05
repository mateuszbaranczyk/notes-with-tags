from fastapi import FastAPI

from app import models

app = FastAPI()

database = {
    "potato": "22kg",
    "garlic": "19kg",
    "onion": "3kg",
}


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.put("/create_note/", response_model=models.Note)
async def create_note(note: models.Note):
    return note
