import time
from config import ALERT_COOLDOWN

class AlertSystem:
    def __init__(self):
        self.last_alert = 0

    def send_alert(self, message):
        if time.time() - self.last_alert > ALERT_COOLDOWN:
            print("🚨 ALERT:", message)
            self.last_alert = time.time()