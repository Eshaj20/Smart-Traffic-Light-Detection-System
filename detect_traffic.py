import torch
import cv2

# Load the YOLOv8 model
model = torch.hub.load('ultralytics/yolov8', 'yolov8', pretrained=True)

def detect_traffic_lights(frame):
    results = model(frame)  # Perform inference on the frame
    return results

def get_light_color(results):
    labels = results.names  # YOLOv8 label names
    detected_objects = results.xywh[0]  # Get object detections

    for obj in detected_objects:
        label = labels[int(obj[5])]  # Get the label (e.g., 'traffic light')
        if label == 'traffic light':
            color = determine_color(obj)  # This function determines the color of the light
            return color
    return "No Traffic Light Detected"

def determine_color(bbox):
    # Dummy implementation to show how you would process the color of a light
    return "Red"  # For now, returning a hardcoded value
