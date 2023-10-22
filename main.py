#from typing import Union

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient

app = FastAPI()

#to connect MongoDB
conn=MongoClient("mongodb+srv://iamishan04:goluishan@cluster0.3gzcrxo.mongodb.net/notes") #""->MongoDB password



