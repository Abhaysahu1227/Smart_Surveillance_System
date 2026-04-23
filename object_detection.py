from ultralytics import YOLO
from config import DETECT_PERSON_ONLY, CONFIDENCE_THRESHOLD

class ObjectDetector:
    def __init__(self):
        self.model = YOLO("yolov8n.pt")

    def detect(self, frame):
        results = self.model(frame)
        detections = []

        for r in results:
            for box in r.boxes:
                conf = float(box.conf[0])
                if conf < CONFIDENCE_THRESHOLD:
                    continue

                cls = int(box.cls[0])
                label = self.model.names[cls]

                if DETECT_PERSON_ONLY and label != "person":
                    continue

                x1, y1, x2, y2 = map(int, box.xyxy[0])
                detections.append((x1, y1, x2, y2, label, conf))

        return detections