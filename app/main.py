from typing import Annotated

from fastapi import Body, FastAPI

from app import models

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.put("/create_note/", response_model=models.Note)
async def create_note(note: Annotated[models.Note, Body(embeded=True)]):
    return note

@app.get("/note/{title}")
async def get_note(title: str):
    return {"title": title} 