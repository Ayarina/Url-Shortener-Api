from fastapi import FastAPI
from typing import Optional
import requests
from pydantic import BaseModel


app = FastAPI(
    title="Decapitador de Urls",
    description="Decapita urls",
    version="69.1",
)

dic = []

class Link(BaseModel):
    url: str
    shortenedurl: str

@app.get("/")
async def root():
    return {"message" : "Decapitador de Urls. Bienvenido sea."}

@app.get("/url/")
async def list_url():
    return dic
    
#@app.get("/url/{url_id}")
#async def list_url(item: Link):
#    return { "url" : item.url}

@app.post("/url/")
async def insert_url(item: Link):
    dic.append(item)
    return dic[-1]


