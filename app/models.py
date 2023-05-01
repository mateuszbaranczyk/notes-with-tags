from enum import Enum
from pydantic import BaseModel


class VegetablesModel(str, Enum):
    onion = "onion"
    garlic = "garlic"
    potato = "potato"


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float


class User(BaseModel):
    username: str
    full_name: str | None = None
