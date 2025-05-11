import cv2

def capture_video():
    cap = cv2.VideoCapture(0)  # Capture from camera
    return cap
