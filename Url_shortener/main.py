from fastapi import Depends, FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Optional

from starlette.responses import RedirectResponse

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI(
    title="URL Beheader",
    description="Decapita urls",
    version="69.1",
)

some_users = {
    "zanahoria":{
        "username": "zanahoria",
        "hashed_password": "hashedcocida",
    },
    "guisante":{
        "username": "guisante",
        "hashed_password": "hashedmuyrico",
    },
}

db = []
takenu = []
takenc = []

class User(BaseModel):
    username: str

class UserInDB(User):
    hashed_password: str

def fake_hash_password(password: str):
    return "hashed" + password

class Link(BaseModel):
    url: str
    custom_name: str

@app.get("/")
async def root():
    return {"message" : "Decapitador de Urls. Bienvenido sea."}

@app.get("/url/")
async def list_url(token: str = Depends(oauth2_scheme)):
    return db

@app.post("/")
async def shorten_url(item: Link, token: str = Depends(oauth2_scheme)):
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

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = some_users.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    
    return {"acces_token": user.username, "token_type": "bearer"}



