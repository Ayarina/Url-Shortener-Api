from fastapi import FastAPI
from typing import Optional

import requests


app = FastAPI()

@app.get("/")
async def root():
    return {"message" : "owo"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}