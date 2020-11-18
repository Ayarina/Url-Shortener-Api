from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

import string
import random

app = FastAPI(
    title="Decapitador de Urls",
    description="Decapita urls",
    version="69.1",
)

dic = []

lista = {
    "sample" : "sample.com"
}
class Link(BaseModel):
    url: str

class Short(BaseModel):
    url: str
    shortened_url: str

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
async def shorten_url(item: Link):
    if item.url in dic:
        return {"url" : item.url, "shortened_url" : d[item.url]}
    else
        shortened_url = random_url(item.url)
        dic.append(item, shortened_url)
        return {"url" : item.url, "shortened_url" : shortened_url}


def random_url(url: str):
    letters = string.ascii_letters
    length = 5
    while len(dic) < length*26*2:
        length = length + 1

    result = 'https://www.UrlDecapitator.com/'.join(random.choice(letters) for i in range(length))
    return result

#####This isn't tested yet