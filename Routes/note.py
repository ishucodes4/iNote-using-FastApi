from fastapi import APIRouter
from models.note import Note

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from config.db import conn
from schemas.note import noteentity,notesentity

note=APIRouter()
templates = Jinja2Templates(directory="templates")#for template directory

#to make sure homepage pehle dikhe
@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs=conn.notes.notes.find_one({})
    for doc in docs:
        newDocs=[]
        newDocs.append({
            "id":doc["_id"],
            "note":doc["note"]
        })
    return templates.TemplateResponse("index.html", {"request": request,"newDocs":newDocs})

@note.post("/")
def add_note(note:Note):
  inserted_note=  conn.notes.notes.insert_one(dict(note))
    return noteentity(inserted_note)
