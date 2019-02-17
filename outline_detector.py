# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         outline_detector
# Description:  轮廓检测器
# Author:       superman
# Date:         2019/2/17
# -------------------------------------------------------------------------------
import cv2
import numpy as np

img = np.zeros((200, 200), dtype=np.uint8)
img[50:150, 50:150] = 255
ret, thresh = cv2.threshold(img, 127, 255, 0)  # 使用阈值对图像进行二值化，返回阈值和二值图像
image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # 指定阈值查找边框
print(contours)  # 轮廓的坐标点
color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)  # 灰度图转换成BGR图
img = cv2.drawContours(color, contours, -1, (0, 255, 0), 2)  # 画轮廓
cv2.imshow("contours", color)
cv2.waitKey()
cv2.destroyAllWindows()
