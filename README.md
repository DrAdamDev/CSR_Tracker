# Object Tracking with CSRT

## Overview
This Python script uses OpenCV's CSRT tracker for object tracking in videos. It allows users to select two objects in the first frame of a video and tracks these objects throughout the video.

## Requirements
- Python 3.x
- OpenCV (cv2)
- NumPy

## Installation
Install the required packages using pip:
```
pip install opencv-python
pip install numpy
```

## Usage
1. Place the video file in the script directory and rename it to 'TrackingVideo.mp4'.
2. Run the script. Two windows will appear for selecting objects (ROIs) in the first frame.
3. After selection, the script tracks these objects and saves the output in 'output.mp4'.

## Output
The output video will be saved in the specified path with bounding boxes around the tracked objects.
