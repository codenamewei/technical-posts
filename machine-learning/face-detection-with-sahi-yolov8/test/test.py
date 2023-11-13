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

import imageio.v3 as iio
from facescan.facedetectionmodel import FaceDetectionModel

from facescan.utils.bbox import Bbox
from facescan.utils.modelselection import ModelSelection

import utils

datapath = "/Users/chiawei.lim/Downloads/buffer/technical-posts/machine-learning/face-detection-with-sahi-yolov8"
inputdatapath = f"{datapath}/edge-input"
outputdatapath = f"{datapath}/edge-output"
modelpath = "/Users/chiawei.lim/Downloads/buffer/model-playground-data/face-detection/models"

yolomodel = os.path.join(modelpath, "yolo_sahi.pt")
sahimodel = os.path.join(modelpath, "yolo_sahi.pt")


if __name__ == "__main__":

    modelpath = dict(YOLO = yolomodel, SAHI = sahimodel, MTCNN = None)

    modeloptions : dict[str, FaceDetectionModel] = utils.load_models(modelpath)

    inputfiles : list[str] = utils.get_all_files(datapath = inputdatapath, targetdatapath = outputdatapath)

    for file in inputfiles:

        if file.endswith(utils.JPG):

            image : np.ndarray = iio.imread(file)

        if file.endswith(utils.PNG):

            #only get the thress channels
        
            image : np.ndarray = iio.imread(file, pilmode='RGB')

        for modelkey, model in modeloptions.items():

            bboxes, probabilities = model.detect(image)

            outimage = image.copy()

            image_with_roi = utils.draw_roi(image = outimage, bboxes=bboxes, probabilities = probabilities)

            outputfilepath = file.replace(inputdatapath, outputdatapath)
            index = outputfilepath.find(".", 20)
            appendedfilepath = outputfilepath[:index] + f"_{modelkey}" + outputfilepath[index:]

            iio.imwrite(appendedfilepath, image_with_roi)
        

