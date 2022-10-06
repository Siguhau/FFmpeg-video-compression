from importlib.metadata import requires

import cv2
import numpy as np
import pytorch_msssim
import torch
from PIL import Image
from pytorch_msssim import ssim
from torch.autograd import Variable

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
m = pytorch_msssim.MSSSIM()


vidcap = cv2.VideoCapture("C:\\Users\\sigur\\Desktop\\hfpsvideos\\hfps.avi")
vidcap2 = cv2.VideoCapture("C:\\Users\\sigur\\Desktop\\demo\\20.mp4")
if not vidcap.isOpened():
    print("1 not open")
if not vidcap2.isOpened():
    print("2 not open")

score = 0
iterations = 0
for x in range(100):
    # vidcap.read()
    success, img1 = vidcap.read()
    success, img2 = vidcap2.read()
    cv2.imwrite("c:\\Users\\sigur\\Desktop\\img1.png", img1)
    cv2.imwrite("c:\\Users\\sigur\\Desktop\\img2.png", img2)

    img1 = np.array(Image.open("c:\\Users\\sigur\\Desktop\\img1.png"))
    img2 = np.array(Image.open("c:\\Users\\sigur\\Desktop\\img2.png"))

    np_img1 = np.array(img1)
    np_img2 = np.array(img2)

    img1 = torch.from_numpy(np_img1).float().unsqueeze(0) / 255.0
    img2 = torch.from_numpy(np_img2).float().unsqueeze(0) / 255.0

    img1 = Variable(img1, requires_grad=False)
    img2 = Variable(img2, requires_grad=False)
    ssim_value12 = ssim(img1, img2).item()
    score += ssim_value12
    iterations += 1
    print("iteration ", iterations, " ssim: ", ssim_value12)
print("average ssim: ", score / iterations)
