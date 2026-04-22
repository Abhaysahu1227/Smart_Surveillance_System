import cv2
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
from config import VIDEO_SOURCE

# OPTIONAL: YOLO (agar install hai to use hoga, warna normal chalega)
from ultralytics import YOLO
model = YOLO("yolov8n.pt")   # lightweight model
YOLO_AVAILABLE = True
print("✅ YOLO model loaded")

def process_frame(frame):
    """
    Frame processing function (YOLO detection optional)
    """
    if YOLO_AVAILABLE:
        results = model(frame)

        for r in results:
            boxes = r.boxes
            for box in boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                conf = float(box.conf[0])
                cls = int(box.cls[0])

                label = f"{model.names[cls]} {conf:.2f}"

                # draw box
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, label, (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    return frame


def main():
    print("🚀 Starting Smart Surveillance System...")

    cap = cv2.VideoCapture(VIDEO_SOURCE)

    if not cap.isOpened():
        print("❌ Error: Camera / Video open nahi hua")
        return

    # FPS calculation
    prev_time = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            print("⚠️ Frame read nahi hua / video end")
            break

        # resize (performance improve)
        frame = cv2.resize(frame, (640, 480))

        # process frame
        frame = process_frame(frame)

        # FPS display
        curr_time = cv2.getTickCount() / cv2.getTickFrequency()
        fps = 1 / (curr_time - prev_time) if prev_time != 0 else 0
        prev_time = curr_time

        cv2.putText(frame, f"FPS: {int(fps)}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        # display
        cv2.imshow("Smart Surveillance", frame)

        # exit key (ESC)
        if cv2.waitKey(1) & 0xFF == 27:
            print("🛑 Exiting...")
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()