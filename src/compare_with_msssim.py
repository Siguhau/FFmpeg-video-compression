import sys

import cv2
import numpy as np
import torch
from PIL import Image
from pytorch_msssim import ssim


class Error(Exception):
    """Base class for other exceptions."""


class CouldNotOpenVideoError(Error):
    """Could not open the specified video."""


class CouldNotLoadFrameError(Error):
    """Could not load the frame."""


def compare_images(img_a, img_b):
    """Returns a ssim score based on the given images."""

    np_img_a = np.array(img_a)
    np_img_b = np.array(img_b)

    torch_img_a = torch.from_numpy(np_img_a).float().unsqueeze(0) / 255.0
    torch_img_b = torch.from_numpy(np_img_b).float().unsqueeze(0) / 255.0
    return ssim(torch_img_a, torch_img_b).item()


def compare_images_from_path(path_a, path_b):
    """Returns a ssim score based on images from the given paths."""

    img_a = Image.open(path_a)
    img_b = Image.open(path_b)
    return compare_images(img_a, img_b)


def compare_videos_from_path(path_a, path_b, frames=1):
    """Returns the average ssim score on the given videos. Add number of frames to read."""

    vidcap_a = cv2.VideoCapture(path_a)
    vidcap_b = cv2.VideoCapture(path_b)

    try:
        if not (vidcap_a.isOpened() and vidcap_b.isOpened()):
            raise (CouldNotOpenVideoError)
    except CouldNotOpenVideoError:
        print("A video could not be opened.")
        sys.exit(1)

    ssim_score = 0
    iterations = 0

    try:
        for _ in range(frames):

            success_a, img_a = vidcap_a.read()
            success_b, img_b = vidcap_b.read()

            if not (success_a and success_b):
                raise (CouldNotLoadFrameError)

            # Unsure of the potential quality loss here.
            img_a_converted = cv2.cvtColor(img_a, cv2.COLOR_BGR2RGB)
            img_b_converted = cv2.cvtColor(img_b, cv2.COLOR_BGR2RGB)

            img_a_pil = Image.fromarray(img_a_converted)
            img_b_pil = Image.fromarray(img_b_converted)
            ssim_score += compare_images(img_a_pil, img_b_pil)
            iterations += 1

    except CouldNotLoadFrameError:
        print("A frame could not be opened, please decrease number of iterations")
        sys.exit(1)

    return ssim_score / iterations
