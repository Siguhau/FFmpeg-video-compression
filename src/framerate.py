import cv2

def framerate(original_path, compressed_path):
    
    "original path: C:\\Users\\sigur\\Desktop\\highframeratevideos\\hpfs2.avi"
    "compressed path: C:\\Users\\sigur\\Desktop\\split\\compressed\\0.mp4"
    
    vidcap = cv2.VideoCapture(original_path)
    vidcap2 = cv2.VideoCapture(compressed_path)

    vidcap.read()
    vidcap2.read()

    fps = int(
        vidcap.get(cv2.CAP_PROP_FPS)
    )  # Might want to go for half of the original fps.
    fps2 = int(
        vidcap2.get(cv2.CAP_PROP_FPS)
    )  # Might want to go for half of the original fps.

    return print(fps, fps2)
