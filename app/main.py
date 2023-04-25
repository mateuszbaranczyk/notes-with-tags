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


# query parameter with max len 50 and default value None as not required
@app.get("/read_item/")
async def read_item(query_param: Annotated[str | None, Query(max_length=8)] = None):
    results = {"item": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if query_param:
        results.update({"q": query_param})
    return results


# use Annotated[list[str] to pass more items in list like /read_more_items/?q=foo&q=bar
# @app.get("/read_more_items/")
# async def read_more_items(query_params: Annotated[list[str] | None, Query()] = None):
#     query_items = {"q": query_params}
#     return query_items
#
# you can create params metadata like this 
@app.get("/read_more_items/")
async def read_more_items(
    query_params: Annotated[
        list[str], Query(title="Items", description="Pass list of products", alias="Products")
    ]
):
    items = {"items": query_params}
    return items
