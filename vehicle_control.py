import RPi.GPIO as GPIO
import time

# Setup for the servo motor
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)  # GPIO Pin for servo motor control
pwm = GPIO.PWM(17, 50)  # 50Hz frequency for servo motor
pwm.start(0)  # Initial position

def move_vehicle(color):
    if color == "Green":
        pwm.ChangeDutyCycle(7)  # Example value for forward motion
    elif color == "Red":
        pwm.ChangeDutyCycle(0)  # Stop motor
    elif color == "Yellow":
        pwm.ChangeDutyCycle(5)  # Slow down or stop partially
    else:
        pwm.ChangeDutyCycle(0)
