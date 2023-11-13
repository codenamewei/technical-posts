#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : codenamewei
# Created Date: 2023-10-27
# Updated Date: 2023-10-27
# version ='1.0'
# ---------------------------------------------------------------------------
from pydantic import BaseModel

class ImageSize(BaseModel):
    
    x : int
    y : int
    channel : int = 3

    @property
    def np_shape(self) -> tuple:

        #numpy shape with height first: (height, width)
        return (self.y, self.x, self.channel)
    

    @property
    def size(self) -> tuple:

        return (self.x, self.y)