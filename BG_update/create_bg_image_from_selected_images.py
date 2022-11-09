import cv2
import numpy as np
import os
import scipy
from PIL import Image

r_medstack = []
g_medstack = []
b_medstack = []

video_name = "ikun"
# selected_frames = [10, 11, 12, 681, 688, 689, 546, 547, 548]
selected_frames = [10, 11, 12, 681, 688, 689, 607, 608, 609]
for frame_id in selected_frames:
    path = os.path.join("frames_" + video_name, "frame" + str(frame_id) + ".jpg")
    frame = cv2.imread(path)
    r_medstack.append(frame[:, :, 0])
    g_medstack.append(frame[:, :, 1])
    b_medstack.append(frame[:, :, 2])

# final_r = np.median(np.array(r_medstack), axis=0)
# final_g = np.median(np.array(g_medstack), axis=0)
# final_b = np.median(np.array(b_medstack), axis=0)

final_r = scipy.stats.mode(np.array(r_medstack)).mode[0]
final_g = scipy.stats.mode(np.array(g_medstack)).mode[0]
final_b = scipy.stats.mode(np.array(b_medstack)).mode[0]

rgb_image_data = np.dstack([final_r, final_g, final_b]).astype(np.uint8)
cv2.imwrite('./bg_from_images.jpg', rgb_image_data)
