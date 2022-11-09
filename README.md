# CS543_Project
Pose to pose on original background

## How to use it
1. Get background\
Recommanded way: update the video name and run `create_bg_image_from_video.py`. The result will be `bg_from_video.jpg`\
Alternative way: update the video name and run `separate_video_to_frames.py` first. Then manually select a number of frames and run `create_bg_image_from_selected_images.py`. The result will be `bg_from_images.jpg`.\
Backup way: check `another_way_to_get_bg.py` and `maybe_another_way_to_get_bg.py`.\

2. Change background\
Run `create_video_and_images_with_new_bg.py`. The result will be `<original_name>_new.mp4`.