from fastapi import FastAPI
import os

app = FastAPI()

# References: https://fastapi.tiangolo.com/advanced/events/

items = {}

@app.on_event("startup")
async def startup_event():

    items["foo"] = {"name": "Fighters"}
    items["bar"] = {"name": "Tenders"}


@app.on_event("shutdown")
def shutdown_event():
    with open("/app/temp/log.txt", mode="a") as log:
        log.write("Application shutdown\n")


@app.get("/items/{item_id}")
async def read_items(item_id: str):
    return items[item_id]

@app.get("/")
async def welcome():
    return dict(message = "Hello World!")