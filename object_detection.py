import cv2
import logging
import keyboard
import time  # Added for camera delay
from ultralytics import YOLO

logging.getLogger("ultralytics").setLevel(logging.ERROR)

model = YOLO("yolov8n.pt")

# Correct camera index and backend for macOS
cap = cv2.VideoCapture(1, cv2.CAP_AVFOUNDATION)

# Stabilization delay
time.sleep(2)

# Set resolution and buffer limit (important for stability)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Failed to grab frame. Check camera index or connection.")
        break

    # HSV Conversion for color detection
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # RGB Conversion for YOLO detection
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = model(frame_rgb)

    if keyboard.is_pressed(" "):
        print("\nObjects in Frame:")
        for result in results:
            for box in result.boxes:
                class_id = int(box.cls[0])
                confidence = float(box.conf[0])
                object_name = model.names[class_id]
                print(f"- {object_name} ({confidence:.2f} confidence)")

    frame_annotated = results[0].plot()
    cv2.imshow("Object Detection", frame_annotated)

    # Show the HSV frame if required for color detection
    # cv2.imshow("HSV Frame", frame_hsv)

    if keyboard.is_pressed("q"):
        break

cap.release()
cv2.destroyAllWindows()
