from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

from starlette.responses import RedirectResponse


app = FastAPI(
    title="Decapitador de Urls",
    description="Decapita urls",
    version="69.1",
)

db = []
takenu = []
takenc = []

class Link(BaseModel):
    url: str
    custom_name: str

@app.get("/")
async def root():
    return {"message" : "Decapitador de Urls. Bienvenido sea."}

@app.get("/url/")
async def list_url():
    return db

@app.post("/")
async def shorten_url(item: Link):
    url = item.url
    custom = item.custom_name
    if {url: custom} in db:
        for i in range(len(db)):
            if {url: custom} == db[i]:
                return {"url": db[i]}
    elif custom in takenc:
        for i in range(len(db)):
            if custom in takenc[i]:
                return {"message": "This custom name is already taken, try again.", "url": db[i]}
    elif url in takenu:
        for i in range(len(db)):
            if url in takenu[i]:
                return {"message": "This url has already a shortened url", "url": db[i]}
    else: 
        db.append({url: custom})
        takenc.append(custom)
        takenu.append(url)
        return {"url" : url, "short": custom}

@app.get("/{short}")
async def redirect(short: str):
    for i in range(len(db)):
        if short in takenc[i]:
            return RedirectResponse(takenu[i])
    return {"message": "URL not defined in the database"}