import ultralytics
from roboflow import Roboflow
from ultralytics import YOLO
from IPython.display import Image
import torch
import cv2

# LOAD PRETARINED
# model = YOLO('yolov8n.pt')  

# Load the trained model (adjust the path to your model file)
# "C:\Users\Sahil\FIRE\runs\detect\train\weights\best.pt"
model = YOLO('best.pt')

# Check if CUDA is available and use GPU if possible
device = 'cuda' if torch.cuda.is_available() else 'cpu'
model.to(device)

# Define the path to your test image or video
test_image_path = 'testimage.png'
test_video_path = 'testvideo.mp4'

# Inference on a video

# cap = cv2.VideoCapture(test_video_path)

# while cap.isOpened():
#     ret, frame = cap.read()
#     if not ret:
#         break

#     # Run inference
#     results = model.predict(frame, conf=0.58, iou=0.45)
    
#     # Visualize results on the frame
#     annotated_frame = results[0].plot()  # Annotate the frame with detections

#     # Display the frame
#     cv2.imshow('YOLOv8 Inference', annotated_frame)
    
#     # Exit if 'q' is pressed
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()


# Inference on a live camera feed
cap = cv2.VideoCapture(0)  # Use 0 for the default camera

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Run inference
    results = model(frame)

    # Visualize results on the frame
    annotated_frame = results[0].plot()

    # Display the frame
    cv2.imshow('YOLOv8 Live Inference', annotated_frame)
    
    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()