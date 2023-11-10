#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : codenamewei
# Created Date: 2023-11-05
# Updated Date: 2023-11-05
# version ='1.0'
# ---------------------------------------------------------------------------
from fastapi import FastAPI, status
from fastapi.responses import RedirectResponse
from item import Item
from redisconnection import RedisConnection
from contextlib import asynccontextmanager
import logging
import sys

logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

redis = RedisConnection()

@asynccontextmanager
async def lifespan(app: FastAPI):
    
    # before server start serving request
    redis.start_connection()
    redis.write(key = "whisky", value = 0)

    yield
    # clean up before server shuts down
    redis.close_connection()

app = FastAPI(lifespan = lifespan)


@app.get("/items/{item_name}")
async def read_items(item_name: str):
    
    return dict(id = redis.read(key = item_name))

@app.post("/items", status_code=status.HTTP_201_CREATED)
async def read_items(item: Item):

    redis.write(key = item.name, value = item.id)

    return dict(message = "ok")

@app.get('/', response_class=RedirectResponse, include_in_schema=False)
async def docs():
    return RedirectResponse(url='/docs')