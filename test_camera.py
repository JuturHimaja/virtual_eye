import cv2

def test_camera(index):
    cap = cv2.VideoCapture(index)
    
    if not cap.isOpened():
        print(f"❌ Camera at index {index} failed to initialize.")
        return

    print(f"✅ Camera at index {index} is working")

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
    # Test index 1 directly since that's your working camera
    test_camera(1)
