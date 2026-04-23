import cv2
from config import SOURCE

class VideoCapture:
    def __init__(self):
        self.cap = cv2.VideoCapture(SOURCE)

    def get_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            return None
        return frame

    def release(self):
        self.cap.release()