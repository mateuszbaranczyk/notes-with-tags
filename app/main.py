from fastapi import FastAPI, Query
from .models import VegetablesModel, Item
from typing import Annotated

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
async def get_vegetables(vege_name: VegetablesModel, short: bool = False):
    if short is True:
        return f"{database[vege_name]}"
    return {f"{vege_name}": database[vege_name]}


@app.put("/item/")
async def create_item(item: Item):
    return item


#query parameter with max len 50 and default value None as not required 
@app.get("/read_items/")
async def read_items(query_param: Annotated[str | None, Query(max_length=8)] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if query_param:
        results.update({"q": query_param})
    return results
