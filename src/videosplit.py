import argparse
import os
import time

import cv2

if __name__ == "__main__":
    start_time = time.time()

    """ Argparser """
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "-o",
        "--output",
        required=False,
        default="output",
        help="output video file name",
    )
    ap.add_argument("-vp", "--videopath", required=True, help="path to video to split")
    ap.add_argument(
        "-dp",
        "--destinationpath",
        required=False,
        default=os.path.abspath(os.getcwd()),
        help="path to where the videos should be saved",
    )
    ap.add_argument(
        "-p",
        "--print",
        required=False,
        default=True,
        help="True/False if program should print anything.",
    )
    args = vars(ap.parse_args())

    """ Arguments """
    output = args["output"]  # Output filename.
    video_path = args["videopath"]  # Location of video to be splitted.
    destination_path = args["destinationpath"]  # Destination of the output files.
    do_print = args["print"]  # If program should print updates or not.
    output1 = "{}\\{}.avi".format(destination_path, output)
    # output2 = "{}\\{}2.avi".format(destination_path, output)

    """ Splitting """
    if do_print:
        print("Splitting video: {} in two, frame by frame".format(video_path))
    vidcap = cv2.VideoCapture(video_path)
    success, image = vidcap.read()
    count = 0
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")  # Be sure to use lower case.
    fps = int(
        vidcap.get(cv2.CAP_PROP_FPS)
    )  # Might want to go for half of the original fps.
    height, width, _ = image.shape

    out1 = cv2.VideoWriter(output1, fourcc, fps, (width, height))
    # out2 = cv2.VideoWriter(output2, fourcc, fps, (width, height))

    # Loop through the video and add to the outputs.
    while success:
        if count % 2 == 0:
            out1.write(image)
        else:
            out1.write(image)
        success, image = vidcap.read()
        count += 1

    # Finish the video files.
    out1.release()
    # out2.release()
    cv2.destroyAllWindows()

    if do_print:
        print("output saved in {}".format(destination_path))
        print("--- finished in %s seconds ---" % (time.time() - start_time))
