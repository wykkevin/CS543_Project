import cv2
import os

folder_name = "converted_images"
new_video_name = folder_name + "_video.mp4"

path = os.path.join(folder_name, "1.png")
image = cv2.imread(path)
h, w, depth = image.shape

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_writer = cv2.VideoWriter(new_video_name, fourcc, 24, (w, h))

if not os.path.exists('result_' + folder_name):
    os.makedirs('result_' + folder_name)

for i in range(1, len(os.listdir(folder_name))):
    fileName = str(i) + '.png'
    path = os.path.join(folder_name, fileName)
    frame = cv2.imread(path)

    name = './result_' + folder_name + '/frame' + fileName
    print('Creating...' + name)
    video_writer.write(frame)

# Release all space and windows once done
video_writer.release()
cv2.destroyAllWindows()
