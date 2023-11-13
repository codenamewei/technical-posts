#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : codenamewei
# Created Date: 2023-10-27
# Updated Date: 2023-11-13
# version ='1.0'
# ---------------------------------------------------------------------------
from facescan.modelselection.yolo.yolomodel import YOLOModel
from facescan.modelselection.mtcnn.mtcnnmodel import MTCNNModel
from facescan.modelselection.sahi.sahimodel import SahiModel
from facescan.utils.bbox import Bbox
import numpy as np
import logging

logger = logging.getLogger()

class FaceDetectionModel:

    model : YOLOModel | SahiModel | MTCNNModel = None
    

    def __init__(self, face_detection_model: YOLOModel | SahiModel | MTCNNModel):

        self.model = face_detection_model
            

    def detect(self, frame: np.array) -> list[Bbox]:


        if len(frame.shape) == 3:

            return self.model.compute_image(frame)
        
        