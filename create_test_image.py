import cv2
import numpy as np

# Create a blank image with colored text
image = np.zeros((480, 640, 3), dtype=np.uint8)
cv2.putText(image, "Test Image", (150, 240), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)

# Save the image
cv2.imwrite("image.jpg", image)

print("✅ Test image created successfully as 'image.jpg'")
