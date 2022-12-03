import cv2
import os
import numpy

folder_name = "remove_converted_images"
new_video_name = folder_name + "_new.mp4"

path = os.path.join(folder_name, "0.png")
image = cv2.imread(path)
h, w, depth = image.shape

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_writer = cv2.VideoWriter(new_video_name, fourcc, 30, (w, h))

if not os.path.exists('result_' + folder_name):
    os.makedirs('result_' + folder_name)

imgBG = cv2.imread("bg_from_video.jpg")
imgBG = cv2.resize(imgBG, (w, h))

for i in range(len(os.listdir(folder_name))):
    fileName = str(i) + '.png'
    path = os.path.join(folder_name, fileName)
    frame = cv2.imread(path)

    frameOut = numpy.uint8(numpy.zeros([h, w, 3]))
    for x in range(h):
        for y in range(w):
            if (frame[x][y] == 0).all():
                frameOut[x][y] = imgBG[x][y]
            else:
                frameOut[x][y] = frame[x][y]
    name = './result_' + folder_name + '/frame' + fileName
    print('Creating...' + name)
    cv2.imwrite(name, frameOut)
    video_writer.write(frameOut)

# Release all space and windows once done
video_writer.release()
cv2.destroyAllWindows()
