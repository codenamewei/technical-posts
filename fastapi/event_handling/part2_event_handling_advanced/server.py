from fastapi import FastAPI, status
from item import Item
from redisconnection import RedisConnection

app = FastAPI()

redis = RedisConnection()

@app.on_event("startup")
async def startup_event():
    
    redis.start_connection()
        
@app.on_event("shutdown")
async def shutdown_event():

    redis.close_connection()

@app.get("/items/{item_id}")
async def read_items(item_id: int):
    
    return dict(name = redis.read(key = item_id))

@app.post("/items", status_code=status.HTTP_201_CREATED)
async def read_items(item: Item):

    redis.write(key = item.id, value = item.name)

    return dict(message = "ok")

@app.get("/")
async def welcome():

    return dict(message = "Welcome to part 2: event handling!")