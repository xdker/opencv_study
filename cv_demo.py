import tensorflow as tf
import cv2
import numpy as np


def avi_trans(input, output='output.avi', mode='MPEG-4'):
    videoCapture = cv2.VideoCapture(input)
    fps = videoCapture.get(cv2.CAP_PROP_FPS)
    size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
            int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    CODE = ()
    if mode == 'YUV':
        CODE = ('I', '4', '2', '0')
    elif mode == "MPEG-1":
        CODE = ('P', 'I', 'M', '1')
    elif mode == "MPEG-4":
        CODE = ('X', 'V', 'I', 'D')
    elif mode == 'OGV':
        CODE = ('T', 'H', 'E', 'O')
    else:
        CODE = ('F', 'L', 'V', '1')
    videoWriter = cv2.VideoWriter(
        output, cv2.VideoWriter_fourcc(CODE), fps, size)
    success, frame = videoCapture.read()
    while success:
        videoWriter.write(frame)
        success, frame = videoCapture.read()


cameraCapture = cv2.VideoCapture(0)
fps = 30
size = (int(cameraCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(cameraCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print(size)
videoWriter = cv2.VideoWriter(
    'cc.avi', cv2.VideoWriter_fourcc('I', '4', '2', '0'), fps, size)
success, frame = cameraCapture.read()
numFrameRemaining = 10 * fps - 1
while success and numFrameRemaining > 0:
    videoWriter.write(frame)
    success, frame = cameraCapture.read()
    numFrameRemaining -= 1
cameraCapture.release()
