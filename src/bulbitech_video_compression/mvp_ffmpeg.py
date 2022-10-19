import os
import time
from subprocess import PIPE, Popen
from vidgear.gears import WriteGear

import cv2
from framerate import get_framerate
from PIL import Image

# list that will contain the images
images = []

# todo: change paths to videos
input_path = '/Users/leonhardbenkert/Documents/FFmpeg-video-compression/assets/in.avi'
output_path = '/Users/leonhardbenkert/Documents/FFmpeg-video-compression/assets/out.avi'

print("Splitting video...")
start_time_split = time.time()

# using cv2 on the input video
capture = cv2.VideoCapture(input_path)

# output_params = {"-vcodec":"libx264", "-crf": 20, "-preset": "fast"} #define (Codec,CRF,preset) FFmpeg tweak parameters for writer
output_params = {
    "-vcodec": "h264_nvenc",
    "-preset": "slow",
} #define (Codec,CRF,preset) FFmpeg tweak parameters for writer
writer = WriteGear(
    output_filename=output_path, compression_mode=True, logging=True, **output_params
)  # Define writer with defined output parameter

while True:
    # reading indivudual frames
    success, frame = capture.read()

    if success:
        # adding the images to the list
        images.append(frame)
    else:
        break

capture.release()
cv2.destroyAllWindows()
print("Time splitting: ", time.time() - start_time_split)

# getting information from the video
height, width, _ = images[0].shape
fps = get_framerate(input_path)

print("Compressing video...")
start_time_compression = time.time()

# todo: change commands for better compression results
"""
command = [
    "ffmpeg",
    "-y",
    "-f",
    "image2pipe",
    "-vcodec",
    "png",
    "-r",
    str(fps),
    "-i",
    "-",
    "-r",
    str(fps),
    output_path,
]
"""

# opening a pipe with ffmpeg
# pipe = Popen(command, stdin=PIPE)

# add all images to pipe
"""
for image in images:
    im = Image.fromarray(image)
    im.save(pipe.stdin, "png")  # todo: is this the right format for ffmpeg?

# closikng the pype and waiting for ffmpeg to finish
pipe.stdin.close()
pipe.wait()
"""

for image in images:

    writer.write(image)

writer.close()


print("Time compressing: ", time.time() - start_time_compression)

print("Control data:")
print(f"Framerate original: {get_framerate(input_path)}")
print(f"Framerate compressed: {get_framerate(output_path)}")
print(
    f"Compression ratio: {os.stat(input_path).st_size / os.stat(output_path).st_size}"
)
