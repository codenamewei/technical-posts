from fastapi import FastAPI
import os

app = FastAPI()

items = dict(foo = {"name": "Fighters"}, 
             bar = {"name": "Tenders"})

@app.get("/items/{item_id}")
async def read_items(item_id: str):
    return items[item_id]

@app.get("/")
async def welcome():
    return dict(message = "Hello World!")