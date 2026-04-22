# ==============================
# SMART SURVEILLANCE CONFIG FILE
# ==============================

# 🔹 INPUT SOURCE
# 0 = webcam
# "data/video.mp4" = video file
VIDEO_SOURCE = 0


# 🔹 FRAME SETTINGS
FRAME_WIDTH = 640
FRAME_HEIGHT = 480


# 🔹 YOLO SETTINGS
YOLO_MODEL = "yolov8n.pt"   # lightweight model
CONFIDENCE_THRESHOLD = 0.5


# 🔹 DETECTION SETTINGS
ENABLE_DETECTION = True   # False karega to sirf camera chalega


# 🔹 DISPLAY SETTINGS
SHOW_FPS = True
WINDOW_NAME = "Smart Surveillance"


# 🔹 SAVE SETTINGS
SAVE_OUTPUT = False   # True karega to video save hoga
OUTPUT_PATH = "output/output.avi"


# 🔹 ALERT SETTINGS (future use)
ENABLE_ALERT = False
ALERT_SOUND = True


# 🔹 SAFE DATA PATH (IMPORTANT)
DATA_PATH = "data"


# 🔹 KEYS
EXIT_KEY = 27   # ESC key