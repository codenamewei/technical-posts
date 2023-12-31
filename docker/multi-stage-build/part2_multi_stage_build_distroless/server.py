from fastapi import FastAPI
from helloworld import mod1

app = FastAPI()

items = {}

@app.on_event("startup")
async def startup_event():

    items["foo"] = {"name": mod1.add_one(0)}
    items["bar"] = {"name": mod1.add_one(1)}

@app.get("/items/{item_id}")
async def read_items(item_id: str):
    return items[item_id]

@app.get("/")
async def welcome():

    return dict(message = "Welcome to part 2: multi stage build with distroless!")