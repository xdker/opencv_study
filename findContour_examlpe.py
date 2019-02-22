# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         findContour_examlpe.py
# Description:  
# Author:       superman
# Date:         2019/2/22
# -------------------------------------------------------------------------------
import cv2
import numpy as np

img = cv2.pyrDown(cv2.imread("./images/statue.jpg", cv2.IMREAD_UNCHANGED))
# 对图片进行二值化
ret, thresh = cv2.threshold(cv2.cvtColor(img.copy(), cv2.COLOR_BGR2GRAY), 127, 255, cv2.THRESH_BINARY)
# 寻找轮廓
image, contours, hier = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for c in contours:
    # 将找到的轮廓框起来
    x, y, w, h = cv2.boundingRect(c)
    # 画出指定大小的矩形
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    # 寻找最小的外接矩形，返回中心坐标，高宽，旋转角
    rect = cv2.minAreaRect(c)
    # 获取矩形的四个顶点
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    cv2.drawContours(img, [box], 0, (0, 0, 255), 3)
    # 寻找轮廓的最小外接圆
    (x, y), radius = cv2.minEnclosingCircle(c)
    center = (int(x), int(y))
    radius = int(radius)
    img = cv2.circle(img, center, radius, (0, 255, 0), 2)
cv2.drawContours(img, contours, -1, (255, 0, 0), 1)
cv2.imshow("contours", img)