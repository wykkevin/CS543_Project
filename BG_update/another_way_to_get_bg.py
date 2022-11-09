import cv2
import numpy as np

c = cv2.VideoCapture("ikun.mp4")
_, f = c.read()

avg1 = np.float32(f)
avg2 = np.float32(f)

while (1):
    ret, f = c.read()

    if ret:
        cv2.accumulateWeighted(f, avg1, 0.1)
        cv2.accumulateWeighted(f, avg2, 0.01)
    else:
        break

res1 = cv2.convertScaleAbs(avg1)
res2 = cv2.convertScaleAbs(avg2)

# cv2.imshow('img', f)
cv2.imwrite('./avg1.jpg', res1)
cv2.imwrite('./avg2.jpg', res2)

cv2.destroyAllWindows()
c.release()
