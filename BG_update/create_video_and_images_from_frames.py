import cv2
import os
from cvzone.SelfiSegmentationModule import SelfiSegmentation

folder_name = "converted_images"
new_video_name = folder_name + "_new.mp4"

path = os.path.join(folder_name, "0.png")
image = cv2.imread(path)
h, w, depth = image.shape

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_writer = cv2.VideoWriter(new_video_name, fourcc, 24, (w, h))

if not os.path.exists('result_' + folder_name):
    os.makedirs('result_' + folder_name)

segmentor = SelfiSegmentation()

imgBG = cv2.imread("bg_from_video.jpg")

for i in range(1, len(os.listdir(folder_name))):
    fileName = str(i) + '.png'
    path = os.path.join(folder_name, fileName)
    frame = cv2.imread(path)

    h, w, layer = frame.shape
    imgBG = cv2.resize(imgBG, (w, h))
    frameOut = segmentor.removeBG(frame, imgBG, threshold=0.4)
    name = './result_' + folder_name + '/frame' + fileName
    print('Creating...' + name)
    cv2.imwrite(name, frameOut)
    video_writer.write(frameOut)

# Release all space and windows once done
video_writer.release()
cv2.destroyAllWindows()
