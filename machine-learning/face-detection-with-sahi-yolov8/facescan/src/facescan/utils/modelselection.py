#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : codenamewei
# Created Date: 2023-10-27
# Updated Date: 2023-11-13
# version ='1.0'
# ---------------------------------------------------------------------------
from enum import Enum

class ModelSelection(str, Enum):

    MTCNN = "MTCNN"
    YOLO = "YOLO"
    SAHI = "SAHI"