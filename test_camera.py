import cv2

def test_camera(index):
    # Force OpenCV to use AVFoundation (Best for macOS)
    cap = cv2.VideoCapture(index, cv2.CAP_AVFOUNDATION)

    if not cap.isOpened():
        print(f"❌ Camera at index {index} failed to initialize.")
        return

    print(f"✅ Camera at index {index} is working")

    # Set camera resolution (common fix for MacBook camera issues)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    while True:
        ret, frame = cap.read()
        if not ret:
            print(f"❌ Failed to grab frame from camera {index}")
            break

        # Display frame dimensions to confirm camera feed is active
        print(f"📷 Frame size: {frame.shape}")
        
        cv2.imshow(f"Camera {index}", frame)

        # Exit on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    test_camera(1)  # Testing index 1 directly
