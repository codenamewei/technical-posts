#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : codenamewei
# Created Date: 2023-10-27
# Updated Date: 2023-10-27
# version ='1.0'
# ---------------------------------------------------------------------------
from pydantic import BaseModel

class Bbox(BaseModel):
    
    x0 : int #box[0]
    y0 : int #box[1]

    x1 : int #box[2]
    y1 : int #box[3]

    @property
    def area(self) -> int:
    
        return (self.x1 - self.x0) * (self.y1 - self.y0)