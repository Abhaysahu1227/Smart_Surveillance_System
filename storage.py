import os
import cv2
import time
from config import SAVE_PATH, SAVE_IMAGES

class Storage:
    def __init__(self):
        os.makedirs(SAVE_PATH, exist_ok=True)

    def save_frame(self, frame):
        if SAVE_IMAGES:
            filename = os.path.join(SAVE_PATH, f"{int(time.time())}.jpg")
            cv2.imwrite(filename, frame)