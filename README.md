
Outdoor Fire Detector
Overview
The Outdoor Fire Detector is a real-time fire detection system designed to identify and alert users to the presence of fires in outdoor environments. Leveraging YOLOv8 (You Only Look Once, version 8) for object detection, this system offers high accuracy and reliability for detecting fires under various environmental conditions.

Features
Real-Time Detection: Detects fires with high accuracy in real-time.
Robust Performance: Handles outdoor conditions effectively.
YOLOv8 Model: Utilizes state-of-the-art YOLOv8 for fire detection.
Installation
Prerequisites

Python 3.8+

YOLOv8: Install using the Ultralytics package.

OpenCV: For video processing.

PyTorch: Deep learning framework.


Steps
Clone the Repository:

bash
Copy code
git clone https://github.com/iamSahilP/outdoor-fire-detector.git

Download YOLOv8 Weights: Follow the instructions provided here to obtain the YOLOv8 weights and place them in the appropriate directory.

Usage
Run the Fire Detector:

bash
Copy code
python detect_fire.py --input path/to/your/video_or_camera_feed
Adjust Parameters:

Modify detect_fire.py to change detection thresholds or other settings.
Configuration
Model Configuration: Modify config.yaml to adjust model parameters.
Thresholds: Adjust detection thresholds in detect_fire.py to tune performance.
Contributing
Contributions are welcome! Please follow these steps to contribute:


Acknowledgements
YOLOv8 by Ultralytics
Python and its vibrant community
Contact
For any questions or support, please reach out to your sahilpatel9112@gmail.com .
