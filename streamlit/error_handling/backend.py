#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : codenamewei
# Created Date: 2024-03-23
# Updated Date: 2024-03-23
# version ='1.0'
# ---------------------------------------------------------------------------
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse

app = FastAPI()


@app.get('/', response_class=RedirectResponse, include_in_schema=False)
async def docs():
    return RedirectResponse(url='/docs')

@app.get("/status")
async def get_server_status():

    return dict(message = "Server is up")


@app.get("/items")
async def get_items():

   raise HTTPException(status_code=404, detail="Item not found")
   

@app.get("/logs")
async def get_logs():

   raise HTTPException(status_code=500, detail="Server overload")
   
    
    


