#!/usr/bin/python
# -*- coding: ascii -*-
# - Jarrod's RasPi Robotics Library

import RPi.GPIO as GPIO # Import the GPIO Library
import time # Import the Time library
import sys
import Tkinter as tk

# Set the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set variables for the GPIO motor pins
#right motors
pinMotorAForwards = 7
pinMotorABackwards = 8
#left motors
pinMotorBForwards = 10 
pinMotorBBackwards = 9

# How many times to turn the pin on and off each second
Frequency = 20
# How long the pin stays on each cycle, as a percent
DutyCycleA = 90.0
DutyCycleB = 50.0
# Settng the duty cycle to 0 means the motors will not turn
Stop = 0.0

# Set the GPIO Pin mode to be Output
GPIO.setup(pinMotorAForwards, GPIO.OUT)
GPIO.setup(pinMotorABackwards, GPIO.OUT)
GPIO.setup(pinMotorBForwards, GPIO.OUT)
GPIO.setup(pinMotorBBackwards, GPIO.OUT)

# Set the GPIO to software PWM at 'Frequency' Hertz
pwmMotorAForwards = GPIO.PWM(pinMotorAForwards, Frequency)
pwmMotorABackwards = GPIO.PWM(pinMotorABackwards, Frequency)
pwmMotorBForwards = GPIO.PWM(pinMotorBForwards, Frequency)
pwmMotorBBackwards = GPIO.PWM(pinMotorBBackwards, Frequency)

# Start the software PWM with a duty cycle of 0 (i.e. not moving)
pwmMotorAForwards.start(Stop)
pwmMotorABackwards.start(Stop)
pwmMotorBForwards.start(Stop)
pwmMotorBBackwards.start(Stop)

#Generic motor control
def GenMotorControl(AForward, ABackword, BForward, BBackword, waitTime):
    pwmMotorAForwards.ChangeDutyCycle(AForward)
    pwmMotorABackwards.ChangeDutyCycle(ABackword)
    pwmMotorBForwards.ChangeDutyCycle(BForward)
    pwmMotorBBackwards.ChangeDutyCycle(BBackword)
    time.sleep(waitTime)

# Turn all motors off
def StopAll():
    print("Stopping motors!")
    GenMotorControl(Stop, Stop, Stop, Stop, 0)

# Turn both motors forwards
def Forwards(t):
    print("Forwards")
    GenMotorControl(DutyCycleA, Stop, DutyCycleA, Stop, t)

# Turn both motors backwards
def Backwards(t):
    print("Backwards")
    GenMotorControl(Stop, DutyCycleA, Stop, DutyCycleA, t)

# Turn Left going forward
def Left(t):
    print("Left Forwards")
    GenMotorControl(DutyCycleA, Stop, DutyCycleB, Stop, t)

#Turn Left going backword 
def LeftB(t):
    print("Left Backwards")
    GenMotorControl(Stop, DutyCycleA, Stop, DutyCycleB, t)

# Turn Right going forward
def Right(t):
    print("Right Forwards")
    GenMotorControl(DutyCycleB, Stop, DutyCycleA, Stop, t)

# Turn Right going backword
def RightB(t):
    print("Right Backwards")
    GenMotorControl(Stop, DutyCycleB, Stop, DutyCycleA, t)
    
# Pivot Left
def Pivot_Left(t):
    print("Pivot Left")
    GenMotorControl(DutyCycleA, Stop, Stop, DutyCycleA, t)

# Pivot Right
def Pivot_Right(t):
    print("Pivot Right")
    GenMotorControl(Stop, DutyCycleA, DutyCycleA, Stop, t)

# Left only Forward
def LeftOnlyForward(t):
    print("Left Only Forward")
    GenMotorControl(DutyCycleA, Stop, Stop, Stop, t)

# Right Only Forward
def RightOnlyForward(t):
    print("Right Only Forward")
    GenMotorControl(Stop, Stop, DutyCycleA, Stop, t)

# Left only Backward
def LeftOnlyBackward(t):
    print("Left Only Backward")
    GenMotorControl(Stop, DutyCycleA, Stop, Stop, t)

# Right Only Backward
def RightOnlyBackward(t):
    print("Right Only Backward")
    GenMotorControl(Stop, Stop, Stop, DutyCycleA, t)

# Exit the script cleanly
def ExitCleanly():
    StopAll()
    print("Cleaning up GPIO pins")
    GPIO.cleanup()
    print("Issue exit command")
    sys.exit()


# Your code to control the robot goes below this line
def Demo():
    RightOnlyForward(3) 
    StopAll()
    LeftOnlyForward(3)
    StopAll()
    RightOnlyBackward(3) 
    StopAll()
    LeftOnlyBackward(3)
    ExitCleanly()

#Command centre, input key from keyboard, appropriate action performed
def command_centre(char):
    slptm = 0.05
    print "Key: ", char
    if char == 'W':
        Forwards(slptm)
    elif char == 'S':
        Backwards(slptm)
    elif char == 'A':
        Left(slptm)
    elif char == 'Z':
        LeftB(slptm)
    elif char == 'C':
        RightB(slptm)
    elif char == 'D':
        Right(slptm)
    elif char == 'Q':
        Pivot_Left(slptm)
    elif char == 'E':
        Pivot_Right(slptm)
    elif char == 'H':
        LeftOnlyBackward(slptm)
    elif char == 'J':
        LeftOnlyForward(slptm)
    elif char == 'K':
        RightOnlyForward(slptm)
    elif char == 'L':
        RightOnlyBackward(slptm)
    elif char == 'X':
        StopAll()
    elif char == 'P':
        Demo()
    elif char == 'M':
        ExitCleanly()
    else:
        print("not used")
        pass

def main():
    #command = tk.Tk()
    #command.bind('<KeyPress>', key_input)
    #command.mainloop()
    while True:
       try:
           input = raw_input("")
           command_centre(input.upper())
       except KeyboardInterrupt:
           ExitCleanly()
       except SystemExit:
           #Exititing
           print("Exiting")
           sys.exit()
       except:
           print("Unexpected error:", sys.exc_info()[0])
           raise
       else:
          time.sleep(0.05)

if __name__ == "__main__":
    main()
