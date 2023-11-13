#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : codenamewei
# Created Date: 2023-11-10
# Updated Date: 2023-11-10
# version ='1.0'
# ---------------------------------------------------------------------------
from facescan.modelselection.abstractmodel import AbstractModel
from facescan.utils.bbox import Bbox
from facenet_pytorch import MTCNN
import numpy as np
import logging

logger = logging.getLogger()

class MTCNNModel(AbstractModel):

    model : MTCNN

    def __init__(self):
        
        logger.info(f"MTCNN Model loaded with device {self.device}")
            

        mtcnn_thresholds = [self.confidence_threshold] * 3 # for three models in mtcnn
        #https://github.com/timesler/facenet-pytorch/blob/6d9028725b8ef9a514e10d19b76508a047d2ab10/models/mtcnn.py#L157
        self.model = MTCNN(keep_all=True, device=self.device, min_face_size = self.min_face_size, thresholds = mtcnn_thresholds, select_largest = False)

    def compute_image(self, frame : np.array) -> (list[Bbox], list[float]):

        # detect face box, probability and landmarks
        #boxes, probs, landmarks = self.mtcnn.detect(frame, landmarks=True)
        rawboxes, probs = self.model.detect(frame, landmarks = False)

        bboxes : list[Bbox] = list()

        if rawboxes is not None:
            for raw_bbox in rawboxes:

                bbox = Bbox(x0 = int(raw_bbox[0]), 
                            y0 = int(raw_bbox[1]), 
                            x1 = int(raw_bbox[2]), 
                            y1 = int(raw_bbox[3]))

                bboxes.append(bbox)

        return bboxes, probs