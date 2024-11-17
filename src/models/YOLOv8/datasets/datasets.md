
BabyMonitor - v1
==============================
## Dataset Folder Structure

The dataset folder structure is as follows:

```
dataset/
└── BabyMonitor.v1i.yolov8/
    ├── train/
    │   ├── images
    │   │		├──image1.png
    │   │		├──image2.png
    │   │		└── ...
    │   │
    │   └── labels
    │			├──image1.txt
    │   	    ├──image2.txt
    │   		└── ...
    ├── valid/
    │   ├── images
    │   │		├──image1.png
    │   │		├──image2.png
    │   │		└── ...
    │   │
    │   └── labels
    │			├──image1.txt
    │   	    ├──image2.txt
    │   		└── ...
    ├── test/
    │   ├── images
    │   │		├──image1.png
    │   │		├──image2.png
    │   │		└── ...
    │   │
    │   └── labels
    │			├──image1.txt
    │   	    ├──image2.txt
    │   		└── ...
    │   
    ├── data.yaml
    ├── README.roboflow.txt
    └── README.dataset.txt
```

This dataset was exported via roboflow.com 

Roboflow is an end-to-end computer vision platform that helps you
* collaborate with your team on computer vision projects
* collect & organize images
* understand and search unstructured image data
* annotate, and create datasets
* export, train, and deploy computer vision models
* use active learning to improve your dataset over time

For state of the art Computer Vision training notebooks you can use with this dataset,
visit https://github.com/roboflow/notebooks

To find over 100k other datasets and pre-trained models, visit https://universe.roboflow.com

The dataset includes 1783 images.
Babysmiling are annotated in YOLOv8 format.

The following pre-processing was applied to each image:
* Auto-orientation of pixel data (with EXIF-orientation stripping)
* Resize to 640x640 (Stretch)

The following augmentation was applied to create 3 versions of each source image:
* 50% probability of horizontal flip
* 50% probability of vertical flip
* Equal probability of one of the following 90-degree rotations: none, clockwise, counter-clockwise, upside-down
* Random rotation of between -15 and +15 degrees
* Random shear of between -4° to +4° horizontally and -4° to +4° vertically
* Random brigthness adjustment of between -11 and +11 percent
* Random Gaussian blur of between 0 and 0.8 pixels
