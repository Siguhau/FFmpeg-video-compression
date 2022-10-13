import cv2


def print_framerates(path_a, path_b):
    """Print framerates of the videos on a given path."""
    fps_a = get_framerate(path_a)
    fps_b = get_framerate(path_b)
    return print(fps_a, fps_b)


def get_framerate(path):
    """Returns the framerate of the video on given path."""
    vidcap = cv2.VideoCapture(path)
    fps = int(vidcap.get(cv2.CAP_PROP_FPS))
    return fps
