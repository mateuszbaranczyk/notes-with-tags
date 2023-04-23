from enum import Enum
from pydantic import BaseModel

class VegetablesModel(str, Enum):
    onion = "onion"
    garlic = "garlic"
    potato = "potato"

class Item(BaseModel):
    name: str
    description: str
    price: float
    tax: float
    