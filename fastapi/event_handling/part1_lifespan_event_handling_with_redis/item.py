#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : codenamewei
# Created Date: 2023-11-05
# Updated Date: 2023-11-05
# version ='1.0'
# ---------------------------------------------------------------------------
from pydantic import BaseModel

class Item(BaseModel):

    name: str
    id: int