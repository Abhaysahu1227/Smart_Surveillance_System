import cv2

class MotionDetector:
    def __init__(self):
        self.prev_frame = None

    def detect(self, frame):
        if self.prev_frame is None:
            self.prev_frame = frame
            return False

        diff = cv2.absdiff(self.prev_frame, frame)
        _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)

        motion = thresh.sum() > 50000

        self.prev_frame = frame
        return motion