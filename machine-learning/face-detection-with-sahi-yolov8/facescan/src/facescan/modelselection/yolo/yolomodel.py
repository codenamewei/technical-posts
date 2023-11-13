#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : codenamewei
# Created Date: 2023-11-10
# Updated Date: 2023-11-10
# version ='1.0'
# ---------------------------------------------------------------------------
from facescan.utils.bbox import Bbox
from facescan.modelselection.abstractmodel import AbstractModel
import numpy as np
import torch
from ultralytics import YOLO

"""
!!DO NOT USE THIS CLASS DIRECTLY!!, use FaceDetectionModel

use FaceDetectionModel

face_detection_model = FaceDetectionModel(YOLOModel(modelpath))
bboxes = face_detection_model.detect(npimage)

"""

class YOLOModel(AbstractModel):

    model : YOLO = None

    def __init__(self, modelpath : str):

        self.model = YOLO(modelpath)

    def compute_image(self, frame: np.array)  -> (list[Bbox], list[float]):
        """
        take in single frame
        
        Return 
        list[Bbox]
        
        outer list: number of faces
        
        list[int]: 4 corners for face roi
             
        """
        # detect face box, probability and landmarks
        results = self.model(frame)
        
        tensor_rawbboxes : torch.Tensor = results[0].boxes.xyxy

        rawprobabilities : list[float] = results[0].boxes.conf.tolist()


        """
        https://docs.ultralytics.com/usage/python/#predict

        From source
        Results usage

        # results would be a list of Results object including all the predictions by default
        # but be careful as it could occupy a lot memory when there're many images,
        # especially the task is segmentation.
        # 1. return as a list
        results = model.predict(source="folder")

        # results would be a generator which is more friendly to memory by setting stream=True
        # 2. return as a generator
        results = model.predict(source=0, stream=True)

        for result in results:
            # Detection
            result.boxes.xyxy   # box with xyxy format, (N, 4)
            result.boxes.xywh   # box with xywh format, (N, 4)
            result.boxes.xyxyn  # box with xyxy format but normalized, (N, 4)
            result.boxes.xywhn  # box with xywh format but normalized, (N, 4)
            result.boxes.conf   # confidence score, (N, 1)
            result.boxes.cls    # cls, (N, 1)

            # Segmentation
            result.masks.data      # masks, (N, H, W)
            result.masks.xy        # x,y segments (pixels), List[segment] * N
            result.masks.xyn       # x,y segments (normalized), List[segment] * N

            # Classification
            result.probs     # cls prob, (num_class, )

        # Each result is composed of torch.Tensor by default,
        # in which you can easily use following functionality:
        result = result.cuda()
        result = result.cpu()
        result = result.to("cpu")
        result = result.numpy()


        """

        rawbboxes : list = tensor_rawbboxes.tolist()

        if rawbboxes is None:
            """No faces detected"""
            return list()
        
        bboxes : list[Bbox] = list()

        probabilities : list[float] = list()

        

        for i, box in enumerate(rawbboxes):

            if rawprobabilities[i] > self.confidence_threshold:

                if (int(box[2] - box[0]) > self.min_face_size) and (int(box[3] - box[1]) > self.min_face_size):

                    probabilities.append(rawprobabilities[i])

                
                    bbox = Bbox(x0 = int(box[0]), y0 = int(box[1]), x1 = int(box[2]), y1 = int(box[3]))

                    if ((bbox.x0 < bbox.x1) and (bbox.y0 < bbox.y1)):

                        bboxes.append(bbox)
                    
                    
                
        return bboxes, probabilities