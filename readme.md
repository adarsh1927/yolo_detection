# Format of Dataset
```
dataset_directory/
├── images/
│   ├── train/
│   │   └── image1.jpg
│   │   └── image2.jpg
│   │   └── ...
│   └── val/ 
│       └── image10.jpg
│       └── image11.jpg
│       └── ...
└── labels/
    ├── train/
    │   └── image1.txt 
    │   └── image2.txt
    │   └── ...
    └── val/
        └── image10.txt
        └── image11.txt
        └── ...
```

# dataset.yaml
```yaml
# Train/val/test sets as 1) dir: path/to/imgs, 2) file: path/to/imgs.txt, or 3) list: [path/to/imgs1, path/to/imgs2, ..]
path: ./customdataset # dataset root dir
train: images/train # train images (relative to 'path') 4 images
val: images/val # val images (relative to 'path') 4 images

# Classes (80 COCO classes)
names:
  0: car
  1: person
```