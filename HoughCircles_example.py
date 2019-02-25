# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         HoughCircles_example.py
# Description:  
# Author:       superman
# Date:         2019/2/24
# -------------------------------------------------------------------------------
import cv2
import numpy as np

coins = cv2.imread("images/water_coins.jpg")
gray_img = cv2.cvtColor(coins, cv2.COLOR_BGR2GRAY)
img = cv2.medianBlur(gray_img, 5)
cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 10, param1=100, param2=30, minRadius=0, maxRadius=0)
circles = np.uint16(np.around(circles))
for i in circles[0, :]:
    cv2.circle(coins, (i[0], i[1]), i[2], (0, 0, 255), 2)
    cv2.circle(coins, (i[0], i[1]), 2, (0, 255, 0), 1)
cv2.imwrite("images/coins.jpg", coins)
cv2.imshow("HoughCirlces", coins)
cv2.waitKey()
cv2.destroyAllWindows()
