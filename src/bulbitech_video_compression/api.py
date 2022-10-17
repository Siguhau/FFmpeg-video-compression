import cv2
import numpy as np
from flask import Flask, request

app = Flask(__name__)

buffer = []


@app.route("/compress", methods=["POST"])
def compress():
    global buffer
    nparr = np.fromstring(request.data, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    buffer.append(img)

    # Do stuff with the video buffer at some point, for instance:
    if len(buffer) > 2:
        width = 100
        height = 100
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        fps = 1
        output_video = cv2.VideoWriter("./test.mp4", fourcc, fps, (width, height))
        for frame in buffer:
            output_video.write(frame)
        output_video.release()
    cv2.destroyAllWindows()
    return "<p>Yello</p>"
