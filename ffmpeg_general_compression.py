"""
    Short script for running ffmpeg on a folder

    To use, ffmpeg must be installed

    Usage with 10 times H.265 compression:
    python c:\path\to\script.py -i c:\path\to\input\ -o c:\path\to\output\ -c libx265 -cr 10
"""
# pip install ffmpeg-python
# might need to install ffmpeg to your computer



import argparse
import os
import subprocess
import time


if __name__ == '__main__':

    # Argparser
    ap = argparse.ArgumentParser(description='Get compression information')
    ap.add_argument("-i", "--input", required=True, help="input folder path")
    ap.add_argument("-o", "--output", required=False, default=os.getcwd(), help="output file")
    ap.add_argument("-c", "--codec", required=True, help="Codec")
    ap.add_argument("-cr", "--compressionRate", required=True, help="Level of compression")
    args = vars(ap.parse_args())

    # Setting arguments
    output = args['output']
    input_arg = args['input']
    codec = args['codec']
    compression_rate = args['compressionRate']
    print(output)
    general_output_path = os.path.join(output, "compressed")
    try:
        print(general_output_path)
        os.mkdir(general_output_path)
    except OSError as e:
        pass

    #Compression with ffmpeg:

    # Find all files in input folder
    input_videos = [f for f in os.listdir(input_arg) if os.path.isfile(os.path.join(input_arg, f))]
    for idx, video in enumerate(input_videos):
        start_time = time.time()
        output_path = os.path.join(general_output_path, f"{idx}.mp4")
        input_path = os.path.join(input_arg, video)
        print(output_path)
        command = f"ffmpeg -hwaccel cuda -i {input_path} -vcodec {codec} -crf {compression_rate} {output_path}"
        print(command)
        subprocess.call(command.split())
        print("time: ", time.time() - start_time)
