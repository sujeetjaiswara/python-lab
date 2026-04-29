from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Define a data model using Pydantic
class Item(BaseModel):
    id: int
    name: str

# In-memory storage
items = [
    Item(id=1, name="Item 1"),
    Item(id=2, name="Item 2")
]

@app.get("/items")
def read_items():
    return items

@app.get("/items/{item_id}")
def read_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/items", status_code=201)
def create_item(item: Item):
    items.append(item)
    return item
