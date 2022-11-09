import cv2
import os
from cvzone.SelfiSegmentationModule import SelfiSegmentation

# https://www.analyticsvidhya.com/blog/2021/07/learn-how-to-do-real-time-background-replacement-using-opencv-and-cvzone/
video_name = "123"
video = cv2.VideoCapture(video_name + ".mp4")
new_video_name = video_name + "_new"

_, frame = video.read()
h, w, depth = frame.shape
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_writer = cv2.VideoWriter(new_video_name, fourcc, 30, (w, h))

if not os.path.exists('result_' + video_name):
    os.makedirs('result_' + video_name)

segmentor = SelfiSegmentation()

imgBG = cv2.imread("bg_from_video.jpg")
currentframe = 0
while True:
    # reading from frame
    ret, frame = video.read()
    if ret:
        h, w, layer = frame.shape
        imgBG = cv2.resize(imgBG, (w, h))
        frameOut = segmentor.removeBG(frame, imgBG, threshold=0.7)
        name = './result_' + video_name + '/frame' + str(currentframe) + '.jpg'
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
