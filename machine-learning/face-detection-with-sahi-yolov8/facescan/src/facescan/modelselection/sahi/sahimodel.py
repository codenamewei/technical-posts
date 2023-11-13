#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : codenamewei
# Created Date: 2023-11-10
# Updated Date: 2023-11-10
# version ='1.0'
# ---------------------------------------------------------------------------
from sahi import AutoDetectionModel
from facescan.utils.bbox import Bbox
from facescan.modelselection.abstractmodel import AbstractModel
from sahi.predict import get_sliced_prediction
from sahi.prediction import PredictionResult, ObjectPrediction
import numpy as np
import logging
import os

logger = logging.getLogger()
class SahiModel(AbstractModel):

    MODEL_TYPE : str = "yolov8"
    model : AutoDetectionModel = None
    slice_partition : int = 256
    overlap_ratio : float = 0.25

    def __init__(self, inmodelpath : str, confidence_threshold: float | None = None, slice_partition : int | None = None, overlap_ratio : float | None = None):

        if not os.path.exists(inmodelpath):

            raise FileNotFoundError(f"{inmodelpath}")
        
        if confidence_threshold:

            self.confidence_threshold = confidence_threshold

        if slice_partition and slice_partition != 0:
            self.slice_partition = slice_partition

        if overlap_ratio and overlap_ratio != 0:

            if self._check_range(overlap_ratio):

                self.overlap_ratio = overlap_ratio

                logger.info(f"Overlap ratio set to {overlap_ratio}")

            else:

                logger.info(f"Overlap ratio defined out of range: {overlap_ratio}. Fall back to default: {self.overlap_ratio}")


        #https://github.com/obss/sahi/blob/main/sahi/auto_model.py
        self.model = AutoDetectionModel.from_pretrained(
            model_type=self.MODEL_TYPE,
            model_path=inmodelpath,
            confidence_threshold=self.confidence_threshold,
            device=self.device, #'cpu', 'cuda:0'
        )

    def compute_image(self, frame: np.array) -> (list[Bbox], list[float]):

        prediction : PredictionResult = get_sliced_prediction(
            frame, 
            self.model,
            slice_height = self.slice_partition,
            slice_width = self.slice_partition,
            overlap_height_ratio = self.overlap_ratio,
            overlap_width_ratio = self.overlap_ratio)

        object_prediction_list : list[ObjectPrediction] = prediction.object_prediction_list

        bboxes : list[Bbox] = list()
        probabilities : list[float] = list()

        for object in object_prediction_list:

            result = object.to_coco_prediction().json

            raw_bbox = result["bbox"]

            if (int(raw_bbox[2]) > self.min_face_size) and (int(raw_bbox[3]) > self.min_face_size):
                
                probabilities.append(object.score.value)

                bbox = Bbox(x0 = int(raw_bbox[0]), 
                            y0 = int(raw_bbox[1]), 
                            x1 = int(raw_bbox[0] + raw_bbox[2]), 
                            y1 = int(raw_bbox[1] + raw_bbox[3]))

                bboxes.append(bbox)


        return bboxes, probabilities