# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         utils.py
# Description:  用于通用处理函数
# Author:       superman
# Date:         2019/2/9
# -------------------------------------------------------------------------------
import cv2
import numpy as np
import scipy.interpolate


def createFlatView(array):
    """Return a 1D view of an array of any dimensionality.将三个信道的图像数，变成一维数组。"""
    flatView = array.view()
    flatView.shape = array.size
    return flatView


def createLookupArray(func, length=256):
    """Return a lookup for whole-number inputs to a function.

    The lookup values are clamped to [0, length - 1].
    返回函数的所有函数值[0,255]。
    """
    if func is None:
        return None
    lookupArray = np.empty(length)
    i = 0
    while i < length:
        func_i = func(i)
        lookupArray[i] = min(max(0, func_i), length - 1)
        i += 1
    return lookupArray


def applyLookupArray(lookupArray, src, dst):
    """Map a source to a destination using a lookup.使用lookup函数映射原始图像。"""
    if lookupArray is None:
        return
    dst[:] = lookupArray[src]


def createCurveFunc(points):
    """Return a function derived from control points."""
    if points is None:
        return None
    numPoints = len(points)
    if numPoints < 2:
        return None
    xs, ys = zip(*points)
    if numPoints < 4:
        kind = 'linear'
        # 'quadratic' is not implemented.
    else:
        kind = 'cubic'
    return scipy.interpolate.interp1d(xs, ys, kind,
                                      bounds_error=False)


def createCompositeFunc(func0, func1):
    """Return a composite of two functions."""
    if func0 is None:
        return func1
    if func1 is None:
        return func0
    return lambda x: func0(func1(x))
