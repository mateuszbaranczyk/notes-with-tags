from fastapi import FastAPI, Body

from app import models
from typing import Annotated

app = FastAPI()



@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.put("/create_note/", response_model=models.Note)
async def create_note(note: Annotated[models.Note, Body(embeded=True)]):
    return note
