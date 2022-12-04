import os
import cv2
import numpy
import scipy

threshold = 10

background_image_name = "converted_images_videobg_from_video.jpg"
background_image = cv2.imread(background_image_name, cv2.IMREAD_GRAYSCALE)
h, w = background_image.shape

image_folder = "converted_images"
removed_image_folder = "remove_" + image_folder

new_video_name = image_folder + "_new_2.mp4"

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_writer = cv2.VideoWriter(new_video_name, fourcc, 24, (w, h))

new_img_bg = cv2.imread("bg_from_video.jpg")
new_img_bg = cv2.resize(new_img_bg, (w, h))

if not os.path.exists(removed_image_folder):
    os.makedirs(removed_image_folder)

for i in range(1, len(os.listdir(image_folder))):
    image_file = str(i) + '.png'
    path = os.path.join(image_folder, image_file)
    original_frame = cv2.imread(path)
    frame = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    gray_new_frame = numpy.zeros([h, w])
    new_frame = numpy.uint8(numpy.zeros([h, w, 3]))
    for i in range(h):
        for j in range(w):
            bg_pixel = background_image[i][j]
            frame_pixel = frame[i][j]
            if bg_pixel > frame_pixel + threshold or bg_pixel < frame_pixel - threshold:
                gray_new_frame[i][j] = frame[i][j]

    # Apply median filter (only when median is 0?)
    gray_new_frame = scipy.signal.medfilt(gray_new_frame, kernel_size=3)
    for i in range(h):
        for j in range(w):
            if gray_new_frame[i][j] != 0:
                new_frame[i][j] = original_frame[i][j]
            else:
                new_frame[i][j] = new_img_bg[i][j]
    print('Generating ' + './' + removed_image_folder + '/' + image_file)
    cv2.imwrite('./' + removed_image_folder + '/' + image_file, new_frame)
    video_writer.write(new_frame)

video_writer.release()
cv2.destroyAllWindows()
