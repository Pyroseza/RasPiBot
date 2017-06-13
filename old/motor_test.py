# CamJam EduKit 3 - Robotics
# Worksheet 3 - Motor Test Code

import RPi.GPIO as GPIO # Import the GPIO Library
import time # Import the Time library

# Set the GPIO modes
GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)

# Set the GPIO Pin mode
GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)

# Turn all motors off
GPIO.output(7, 0)
GPIO.output(8, 0)
GPIO.output(9, 0)
GPIO.output(10, 0)

# Turn the right motor forwards
print("9 off")
GPIO.output(9, 1)
print("10 on")
GPIO.output(10, 0)

# Turn the left motor forwards
print("7 on")
GPIO.output(7, 1)
print("8 off")
GPIO.output(8, 0)

# Wait for 2 seconds
print("sleep 2 secs")
time.sleep(2)

# Reset the GPIO pins (turns off motors too)
GPIO.cleanup()
