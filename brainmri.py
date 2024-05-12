import cv2
import matplotlib.pyplot as plt
import numpy as np

# Assuming assets folder is in the same directory as your script
image_path = "assets/mribrain.jpg"

# Read the image using OpenCV (assuming it's BGR format)
image_bgr = cv2.imread(image_path)

# Convert to RGB if necessary (depending on your processing needs)
image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)

# Extract the ROI (Region of Interest) based on coordinates
x_min, y_min, x_max, y_max = 0, 0, 200, 200
image_roi = image_rgb[y_min:y_max, x_min:x_max]

# You can now process the ROI further (e.g., convert to grayscale)
image_gray = cv2.cvtColor(image_roi, cv2.COLOR_BGR2GRAY)

# Show the ROI
plt.imshow(image_gray, cmap='gray')
plt.title('Extracted ROI')
plt.show()
