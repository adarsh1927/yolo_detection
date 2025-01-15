import torch
from ultralytics import YOLO

# # create From Scratch
# model = YOLO('yolov11n-seg.yaml') 


# # Load old weight of detetcion model initialize segmentaion architecture from yaml
# model = YOLO("yolo11n-seg.yaml").load("yolo11n.pt")

# Load the pretrained model weight completely
# equvalet to YOLO("yolo11n-seg.yaml").load("yolo11n-seg.pt") in sense 
model = YOLO('yolo11n-seg.pt')  #is best # or any other YOLO segmentation model


# Load a dataset for fine tune or training
# Replace 'path/to/dataset.yaml' with my dataset configuration file
train_results = model.train(data='dataset.yaml', epochs=100, imgsz=640) 

# Evaluate the model
val_results = model.val() 

# # Export the model
# # we can choose different export formats and arguments
# # model.export(format='onnx')