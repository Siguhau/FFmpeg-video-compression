"""
    Usage with 10 times H.265 compression:
    python c:\path\to\script.py -i c:\path\to\input\ -o c:\path\to\output\ -c libx265 -cr 10
"""

import os
import subprocess
import time


def general_compression(input_folder, output_path, codec, cr):
    general_output_path = os.path.join(output_path, "compressed")
    try:
        os.mkdir(general_output_path)
    except OSError:
        pass

    # Find all files in input folder
    input_videos = [
        f
        for f in os.listdir(input_folder)
        if os.path.isfile(os.path.join(input_folder, f))
    ]
    for idx, video in enumerate(input_videos):
        start_time = time.time()
        output_path = os.path.join(general_output_path, f"{idx}.mp4")
        input_path = os.path.join(input_folder, video)
        print(output_path)
        command = f"ffmpeg -hwaccel cuda -i {input_path} -vcodec {codec} -crf {cr} {output_path}"
        print(command)
        subprocess.call(command.split())
        print("time: ", time.time() - start_time)
