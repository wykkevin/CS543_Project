import cv2
import os
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import numpy as np

# https://www.analyticsvidhya.com/blog/2021/07/learn-how-to-do-real-time-background-replacement-using-opencv-and-cvzone/
video_name = "123"
video = cv2.VideoCapture(video_name + ".mp4")
new_video_name = video_name + "_grabcut_new"

_, frame = video.read()
h, w, depth = frame.shape
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_writer = cv2.VideoWriter(new_video_name, fourcc, 30, (w, h))

if not os.path.exists('result_grabcut_' + video_name):
    os.makedirs('result_grabcut_' + video_name)

segmentor = SelfiSegmentation()

new_background_image = cv2.imread("bg_from_video.jpg")
currentframe = 0
while True:
    # reading from frame
    ret, frame = video.read()
    if ret:
        h, w, layer = frame.shape
        new_background_image = cv2.resize(new_background_image, (w, h))

        # Grabcut
        mask = np.zeros(frame.shape[:2], np.uint8)
        backgroundModel = np.zeros((1, 65), np.float64)
        foregroundModel = np.zeros((1, 65), np.float64)
        rectangle = (0, 0, h, w)
        cv2.grabCut(frame, mask, rectangle,
                    backgroundModel, foregroundModel,
                    3, cv2.GC_INIT_WITH_RECT)
        mask = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
        frameOut = frame * mask[:, :, np.newaxis]

        # frameOut = segmentor.removeBG(frame, new_background_image, threshold=0.7)
        name = './result_grabcut_' + video_name + '/framea' + str(currentframe) + '.jpg'
        print('Creating...' + name)
        cv2.imwrite(name, frameOut)
        video_writer.write(frameOut)
        currentframe += 1
    else:
        break

# Release all space and windows once done
video.release()
video_writer.release()
cv2.destroyAllWindows()
