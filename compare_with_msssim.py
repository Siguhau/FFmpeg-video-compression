import torch
import cv2
from pytorch_msssim import ssim
from PIL import Image
import numpy as np
from torch.autograd import Variable
import sys


def compare_images(img_a, img_b):

    img_a = np.array(img_a)
    img_b = np.array(img_b)

    np_img_a = np.array(img_a)
    np_img_b = np.array(img_b)

    img_a = torch.from_numpy(np_img_a).float().unsqueeze(0) / 255.0
    img_b = torch.from_numpy(np_img_b).float().unsqueeze(0) / 255.0

    img_a = Variable(img_a, requires_grad=False)
    img_b = Variable(img_b, requires_grad=False)
    return ssim(img_a, img_b).item()


def compare_images_from_path(path_a, path_b):

    img_a = Image.open(path_a)
    img_b = Image.open(path_b)
    return compare_images(img_a, img_b)


class Error(Exception):
    """Base class for other exceptions."""


class CouldNotOpenVideoError(Error):
    """Could not open the specified video."""


class CouldNotLoadFrameError(Error):
    """Could not load the frame."""


def compare_videos_from_path(path_a, path_b, frames=1):
    
    vidcap_a = cv2.VideoCapture(path_a)
    vidcap_b = cv2.VideoCapture(path_b)

    try:
        if not vidcap_a.isOpened():
            raise (CouldNotOpenVideoError)
        if not vidcap_b.isOpened():
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

            if not success_a:
                raise (CouldNotLoadFrameError)
            if not success_b:
                raise (CouldNotLoadFrameError)

            # Unsure of the potential quality loss here.
            img_a_converted = cv2.cvtColor(img_a, cv2.COLOR_BGR2RGB)
            img_b_converted = cv2.cvtColor(img_b, cv2.COLOR_BGR2RGB)

            img_a_pil = Image.fromarray(img_a_converted)
            img_b_pil = Image.fromarray(img_b_converted)
            ssim_score += compare_images(img_a_pil, img_b_pil)
    except CouldNotLoadFrameError:
        print("A frame could not be opened, please decrease number of iterations")
        sys.exit(1)

    print("average ssim: ", ssim_score / iterations)