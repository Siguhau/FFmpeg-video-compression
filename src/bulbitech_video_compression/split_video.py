import os

import cv2
from framerate import get_framerate


def split_video(input_path, output_path, output_name):
    """Split a video frame by frame and save them as videos."""

    # Create output folder
    try:
        os.mkdir(output_path)
    except OSError:
        pass

    output1_path = os.path.join(output_path, f"{output_name}_1.avi")
    output2_path = os.path.join(output_path, f"{output_name}_2.avi")

    # Read video
    input_video = cv2.VideoCapture(input_path)
    success, image = input_video.read()
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    height, width, _ = image.shape
    # Might want to go for half of the original fps
    fps = get_framerate(input_path)
    output_video_1 = cv2.VideoWriter(output1_path, fourcc, fps, (width, height))
    output_video_2 = cv2.VideoWriter(output2_path, fourcc, fps, (width, height))

    # Split video
    count = 0
    while success:
        if count % 2 == 0:
            output_video_1.write(image)
        else:
            output_video_2.write(image)
        success, image = input_video.read()
        count += 1

    output_video_1.release()
    output_video_2.release()
    cv2.destroyAllWindows()
