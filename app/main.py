from fastapi import FastAPI
from .models import VegetablesModel, Item

app = FastAPI()

database = {
    "potato": "22kg",
    "garlic": "19kg",
    "onion": "3kg",
}


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/vegetables/{vege_name}")
def get_vegetables(vege_name: VegetablesModel, short: bool = False):
    if short is True:
        return f"{database[vege_name]}"
    return {f"{vege_name}": database[vege_name]}


@app.put("/items/")
def create_item(item: Item):
    return item

#TODO https://fastapi.tiangolo.com/tutorial/query-params-str-validations/