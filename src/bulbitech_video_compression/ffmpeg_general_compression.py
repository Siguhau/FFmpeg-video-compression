import os
import subprocess
import time


def general_compression(
    input_folder, output_path, codec="libx265", compression_rate=20, use_gpu=False
):
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
        command = f"ffmpeg -i {input_path} -vcodec {codec} -crf {compression_rate} {output_path}"
        if use_gpu:
            output_path = os.path.join(general_output_path, f"{idx}.avi")
            command = f"ffmpeg -i {input_path} -c:v h264_nvenc -preset:v p7 -tune hq -cq:v 19 -rc:v vbr {output_path}"
        subprocess.call(command.split())
        print("time: ", time.time() - start_time)
