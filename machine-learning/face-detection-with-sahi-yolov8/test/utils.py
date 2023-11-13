#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : codenamewei
# Created Date: 2023-10-27
# Updated Date: 2023-10-27
# version ='1.0'
# ---------------------------------------------------------------------------
import os
import numpy as np
from facescan.facedetectionmodel import FaceDetectionModel
from facescan.modelselection.yolo import YOLOModel
from facescan.modelselection.sahi import SahiModel
from facescan.modelselection.mtcnn import MTCNNModel
from facescan.utils.modelselection import ModelSelection
from facescan.utils.bbox import Bbox

import cv2

JPG = ".jpg"
PNG = ".png"

def draw_roi(image : np.ndarray, bboxes : list[Bbox], color : (int, int, int) = (217, 2, 125), probabilities : list[float] = None, text_color : (int, int, int) = (217, 2, 125)) -> np.ndarray:

    if probabilities is None:
        for bbox in bboxes:

            cv2.rectangle(image, (bbox.x0, bbox.y0), (bbox.x1, bbox.y1), color, 3)
    
    else:

        for i, bbox in enumerate(bboxes):

            probability = str(int(probabilities[i] * 100)) + "%"

            cv2.rectangle(image, (bbox.x0, bbox.y0), (bbox.x1, bbox.y1), color, 3)
            cv2.putText(image, text = probability, org = (bbox.x1 + 5, bbox.y1 + 5), fontFace = cv2.FONT_HERSHEY_SIMPLEX, fontScale = 0.5, thickness = 2, color = text_color)


    return image

def raise_exception_if_model_file_not_exist(allmodels : list[str]):

    for modelfilepath in allmodels:

        if modelfilepath and not os.path.exists(modelfilepath):

            raise FileNotFoundError(f"Model file {modelfilepath} not found. Program abort")

def raise_exception_if_imagefolder_not_exist(folderpath : str):

    if not os.path.exists(folderpath):

        raise FileNotFoundError(f"Folder {folderpath} not found. Program abort")

def get_all_files(datapath : str, targetdatapath : str) -> list[str]:

    raise_exception_if_imagefolder_not_exist(folderpath = datapath)

    absfilepath : list[str] = list()

    subdatapath = os.walk(datapath)

    for path in subdatapath:

        folderpath = path[0]

        outputfolderpath = folderpath.replace(datapath, targetdatapath)

        if not os.path.exists(outputfolderpath):

            os.makedirs(outputfolderpath)

        for filename in path[2]:

            if filename.endswith(JPG) or filename.endswith(PNG):

                absfilepath.append(os.path.join(folderpath, filename))

    return absfilepath

def load_models(modelkeyvalue : dict[str, str]) -> dict[str, FaceDetectionModel]:

    raise_exception_if_model_file_not_exist(allmodels = list(modelkeyvalue.values()))

    modelloader = dict()

    for modelkey, modelfilepath in modelkeyvalue.items():

        model = None

        if modelkey == ModelSelection.YOLO.value:

            model = YOLOModel(modelfilepath)
        
        elif modelkey ==  ModelSelection.SAHI.value:

            model = SahiModel(modelfilepath)

        elif modelkey == ModelSelection.MTCNN.value:

            model = MTCNNModel()

        if model:
            modelloader[modelkey] = FaceDetectionModel(model)

    return modelloader