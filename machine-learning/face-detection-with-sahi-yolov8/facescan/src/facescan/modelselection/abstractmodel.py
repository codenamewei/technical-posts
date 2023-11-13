#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : codenamewei
# Created Date: 2023-11-10
# Updated Date: 2023-11-13
# version ='1.0'
# ---------------------------------------------------------------------------

from abc import ABC, abstractmethod
from facescan.utils.bbox import Bbox
import numpy as np
import logging
import torch

logger = logging.getLogger()

class AbstractModel(ABC):

    _min_face_size : int = 20
    _confidence_threshold: float = 0.65
    _device : str = None

    @property
    def min_face_size(self):

        return self._min_face_size

    @property
    def confidence_threshold(self):

        return self._confidence_threshold
    
    @property
    def device(self):

        self._set_to_cuda_if_available()

        return self._device
    
    def _set_to_cuda_if_available(self):

        self._device = 'cuda:0' if torch.cuda.is_available() else 'cpu'
        
    
    @confidence_threshold.setter
    def confidence_threshold(self, confidence_threshold : float):

        if self._check_range(confidence_threshold):

            self._confidence_threshold = confidence_threshold

            logger.info(f"Confidence threshold set to {confidence_threshold}")

        else:

            logger.info(f"Confidence threshold defined out of range: {confidence_threshold}. Fall back to default: {self._confidence_threshold}")


    def _check_range(self, value : float) -> bool:

        return True if ((value < 1.0) and (value > 0.0)) else False

    @abstractmethod
    def compute_image(self, frame : np.array) -> (list[Bbox], list[float]):
        """
        list[Bbox]: bbox with x0, y0, x1, y1
        list[float]: probability of each Bbox
        """
        
        raise NotImplementedError("subclasses should implement this!")