# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         face_detection.py
# Description:  
# Author:       superman
# Date:         2019/2/24
# -------------------------------------------------------------------------------
import cv2

filename = "images/people.jpg"


def detect(filename):
    face_cascade = cv2.CascadeClassifier('./cascades/haarcascade_frontalface_default.xml')
    img = cv2.imread(filename)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.namedWindow("Face detection!")
    cv2.imshow("Face Detected!", img)
    cv2.imwrite("./images/face.jpg", img)
    cv2.waitKey(0)


if __name__ == '__main__':
    detect(filename)
