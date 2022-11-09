import cv2
import os

video_name = "ikun"
video = cv2.VideoCapture(video_name + ".mp4")

if not os.path.exists("frames_" + video_name):
    os.makedirs("frames_" + video_name)
# frame
currentframe = 0

while True:
    # reading from frame
    ret, frame = video.read()
    if ret:
        # if video is still left continue creating images
        name = './frames_' + video_name + '/frame' + str(currentframe) + '.jpg'
        print('Creating...' + name)
        cv2.imwrite(name, frame)
        currentframe += 1
    else:
        break

# Release all space and windows once done
video.release()
cv2.destroyAllWindows()
