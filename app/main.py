from fastapi import FastAPI, Query, Path, Body, Cookie, status
from .models import VegetablesModel, Item, User
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


@app.put("/item/", status_code=status.HTTP_201_CREATED)
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


# validation can be used also on path parameters (example with numeric validation)
# gt: greater than
# ge: greater than or equal
# lt: less than
# le: less than or equal
@app.get("/read_item_id/{path_param}")
async def read_item_id(
    path_param: Annotated[int, Path(description="The ID of the item to get", ge=0, le=1000)]
):
    item_id = {"requested_item_id": path_param}
    return item_id


# you can put to parameters  multiple models and also use `Body to pass another key to existing body`
# without Body it would be query parameter
# Body also has all the same extra validation and metadata parameters as Query,Path and others you will see later.
@app.get("/item_for_user/")
async def item_for_user(item: Item,  user_name: User, importanace: Annotated[int, Body()]):
    result = {"item": item, "user": user_name, "importanace": importanace}
    return result

# Cookies and Headers are used the same way as below
@app.get("/item_with_ads/")
async def item_with_ads(ads_id: Annotated[str | None, Cookie()] = None):
    return {"ads_id": ads_id}