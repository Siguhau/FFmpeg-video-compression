import cv2
vidcap = cv2.VideoCapture("C:\\Users\\sigur\\Desktop\\highframeratevideos\\hpfs2.avi")
vidcap2 = cv2.VideoCapture("C:\\Users\\sigur\\Desktop\\split\\compressed\\0.mp4")

vidcap.read()
vidcap2.read()

fps = int(vidcap.get(cv2.CAP_PROP_FPS)) # Might want to go for half of the original fps.
fps2 = int(vidcap2.get(cv2.CAP_PROP_FPS)) # Might want to go for half of the original fps.

print(fps)
print(fps2)
