import cv2
import numpy as np
import scipy

c = cv2.VideoCapture("ikun.mp4")
r_medstack = []
g_medstack = []
b_medstack = []

while 1:
    ret, frame = c.read()

    if ret:
        r_medstack.append(frame[:, :, 0])
        g_medstack.append(frame[:, :, 1])
        b_medstack.append(frame[:, :, 2])
    else:
        break

final_r = scipy.stats.mode(np.array(r_medstack)).mode[0]
final_g = scipy.stats.mode(np.array(g_medstack)).mode[0]
final_b = scipy.stats.mode(np.array(b_medstack)).mode[0]
rgb_image_data = np.dstack([final_r, final_g, final_b]).astype(np.uint8)
cv2.imwrite('./bg_from_video.jpg', rgb_image_data)

cv2.destroyAllWindows()
c.release()
