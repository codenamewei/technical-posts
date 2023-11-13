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
from modelselection import ModelSelection

import utils

inputdatapath = "edge-input"
outputdatapath = "edge-output"
modelpath = "/Users/chiawei.lim/Downloads/buffer/model-playground-data/face-detection/models"

yolomodel = os.path.join(modelpath, "yolo_sahi.pt")#"yolo.onnx")
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

            bboxes : list[Bbox] = model.detect(image)

            outimage = image.copy()

            image_with_roi = utils.draw_roi(image = outimage, bboxes=bboxes)

            outputfilepath = file.replace(inputdatapath, outputdatapath)
            index = outputfilepath.find(".")
            appendedfilepath = outputfilepath[:index] + f"_{modelkey}" + outputfilepath[index:]

            print(appendedfilepath)

            iio.imwrite(appendedfilepath, image_with_roi)
        

