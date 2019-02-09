# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         filters
# Description: 定义一下滤波器
# Author:       superman
# Date:         2019/2/9
# -------------------------------------------------------------------------------
import cv2
import numpy as np
import utils


def strokeEdges(src, dst, blurKsize=7, edgeKsize=5):
    if blurKsize >= 3:
        blurredSrc = cv2.medianBlur(src, blurKsize)
        graySrc = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
