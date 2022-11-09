import cv2
import os
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation

# https://www.analyticsvidhya.com/blog/2021/07/learn-how-to-do-real-time-background-replacement-using-opencv-and-cvzone/
ikun = cv2.VideoCapture("ikun.mp4")
# fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
fgbg = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=50, detectShadows=True)
a = fgbg.getBackgroundImage()
print(a)

while (1):
    ret, frame = ikun.read()
    fgmask = fgbg.apply(frame)
    cv2.imshow('frame', fgmask)
    k = cv2.waitKey(30) & 0xff

    if k == 27:
        break