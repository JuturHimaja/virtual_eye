import cv2

# Test each camera index
for index in [0, 1]:
    cap = cv2.VideoCapture(index)
    if cap.isOpened():
        print(f"✅ Camera at index {index} is working")
        while True:
            ret, frame = cap.read()
            if not ret:
                print(f"❌ Failed to grab frame from camera {index}")
                break

            cv2.imshow(f"Camera {index}", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
    else:
        print(f"❌ Camera at index {index} failed to initialize")
