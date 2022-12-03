import cv2
import os
from cvzone.SelfiSegmentationModule import SelfiSegmentation

folder_name = "train_img"
new_folder_name = folder_name + "_new_bg"

path = os.path.join(folder_name, "frame000001.png")
image = cv2.imread(path)
h, w, depth = image.shape

if not os.path.exists(new_folder_name):
    os.makedirs(new_folder_name)

segmentor = SelfiSegmentation()

imgBG = cv2.imread("bg_from_video.jpg")

count = 0
for fileName in os.listdir(folder_name):

    if count >10:
        break
    count+=1
    path = os.path.join(folder_name, fileName)
    frame = cv2.imread(path)

    h, w, layer = frame.shape
    imgBG = cv2.resize(imgBG, (w, h))
    frameOut = segmentor.removeBG(frame, imgBG, threshold=0.6)
    name = './' + new_folder_name + '/' + fileName
    print('Creating...' + name)
    cv2.imwrite(name, frameOut)

# Release all space and windows once done
cv2.destroyAllWindows()
