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

dic = {}

class Link(BaseModel):
    url: str

@app.get("/")
async def root():
    return {"message" : "Decapitador de Urls. Bienvenido sea."}

@app.get("/url/")
async def list_url():
    return dic
    
@app.post("/url/")
async def shorten_url(item: Link):
    if item.url in dic:
        return {"url" : item.url, "shortened_url" : dic[item.url]}
    else:
        shortened_url = random_url(item.url)
        dic[item.url] = shortened_url
        #dic.append(item)
        return {"url" : item.url, "shortened_url" : shortened_url}    


def random_url(url: str):
    letters = string.ascii_letters
    length = 6
    result = 'https://www.UrlDecapitator.com/'.join(random.choice(letters) for i in range(length))
    return result

#####This isn't tested yet