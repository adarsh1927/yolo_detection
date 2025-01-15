from ultralytics import YOLO
import cv2
import numpy as np
import random

# Load a model
model = YOLO("yolo11n.pt")  # load an official model
# model = YOLO("path/to/best.pt")  # load a custom model

# Predict with the model
results = model("/car.jpg")  # predict on an image

for result in results:
    img = result.orig_img
    # Plot the boxes and labels on the original image
    annotated_frame = result.plot() 

cv2.imshow("Detected Objects", annotated_frame)
key = cv2.waitKey(0)
cv2.destroyAllWindows()
