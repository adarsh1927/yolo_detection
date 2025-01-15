from ultralytics import YOLO
import cv2
import numpy as np
import random

# Load a model
model = YOLO("yolo11n.pt")  # load an official model
# model = YOLO("path/to/best.pt")  # load a custom model

cap = cv2.VideoCapture('./rahuls/video.mp4')
while (cap.isOpened()):
    ret, frame = cap.read()
    height, width, c = frame.shape

    # aspect resizing
    if height < width:
        aspect = height/width
        width = 400
        height = int(width * aspect)
    else:
        aspect = width/height
        height = 400
        width = int(height * aspect)

    frame = cv2.resize(frame, (width, height), cv2.INTER_NEAREST)

    # Predict with the model
    results = model(frame.copy())  #.copy avoid changing orignal

    # get mask and draw segmentation
    for result in results:
        img = result.orig_img
        annotated_frame = result.plot() 
    cv2.imshow("original ", frame) 
    cv2.imshow("Segmented video", img)
    cv2.imshow("Segmentations", annotated_frame)

    key = cv2.waitKey(25)
    if key == 27:
        break

cv2.destroyAllWindows()