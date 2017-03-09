#!/usr/bin/python
# -*- coding: ascii -*-
# - Jarrod's RasPi Robotics Library

import RPi.GPIO as GPIO # Import the GPIO Library
import time # Import the Time library
import sys
import Tkinter as tk

# Set the GPIO modes
GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)

# Set variables for the GPIO motor pins
#left motors
pinMotorLeftForwards = 7
pinMotorLeftBackwards = 8
#right motors
pinMotorRightForwards =  9
pinMotorRightBackwards = 10

# How many times to turn the pin on and off each second
Frequency = 60
# How long the pin stays on each cycle, as a percent
DutyCycleHigh = 90.0
DutyCycleLow = 60.0
# Settng the duty cycle to 0 means the motors will not turn
DutyCycleStop = 0.0

#Keywords
Fwd="Forwards"
Bwd="Backwards"
Stp="Stop"

# Set the GPIO Pin mode to be Output
GPIO.setup(pinMotorLeftForwards, GPIO.OUT)
GPIO.setup(pinMotorLeftBackwards, GPIO.OUT)
GPIO.setup(pinMotorRightForwards, GPIO.OUT)
GPIO.setup(pinMotorRightBackwards, GPIO.OUT)

# Set the GPIO to software PWM at 'Frequency' Hertz
pwmMotorLeftForwards = GPIO.PWM(pinMotorLeftForwards, Frequency)
pwmMotorLeftBackwards = GPIO.PWM(pinMotorLeftBackwards, Frequency)
pwmMotorRightForwards = GPIO.PWM(pinMotorRightForwards, Frequency)
pwmMotorRightBackwards = GPIO.PWM(pinMotorRightBackwards, Frequency)

# Start the software PWM with a duty cycle of 0 (i.e. not moving)
pwmMotorLeftForwards.start(DutyCycleStop)
pwmMotorLeftBackwards.start(DutyCycleStop)
pwmMotorRightForwards.start(DutyCycleStop)
pwmMotorRightBackwards.start(DutyCycleStop)

#Generic motor control
def GenMotorControl(LeftDirection, LeftSpeed, RightDirection, RightSpeed, waitTime):
    #Left motors
    print("Left motor: ", LeftDirection, ", speed: ", LeftSpeed) 
    if LeftDirection == "Forwards":
        pwmMotorLeftForwards.ChangeDutyCycle(LeftSpeed)
        pwmMotorLeftBackwards.ChangeDutyCycle(DutyCycleStop)
    elif LeftDirection == "Backwards":
        pwmMotorLeftForwards.ChangeDutyCycle(DutyCycleStop)
        pwmMotorLeftBackwards.ChangeDutyCycle(LeftSpeed)
    else:
        pwmMotorLeftForwards.ChangeDutyCycle(DutyCycleStop)
        pwmMotorLeftBackwards.ChangeDutyCycle(DutyCycleStop)
    #Right motors
    print("Right motor: ", RightDirection, ", speed: ", RightSpeed) 
    if RightDirection == "Forwards":
        pwmMotorRightForwards.ChangeDutyCycle(RightSpeed)
        pwmMotorRightBackwards.ChangeDutyCycle(DutyCycleStop)
    elif RightDirection == "Backwards":
        pwmMotorRightForwards.ChangeDutyCycle(DutyCycleStop)
        pwmMotorRightBackwards.ChangeDutyCycle(RightSpeed)
    else:
        pwmMotorRightForwards.ChangeDutyCycle(DutyCycleStop)
        pwmMotorRightBackwards.ChangeDutyCycle(DutyCycleStop)
    #GenMotorControlSafetyNet(pwmLeftMotorForwards, pwmLeftMotorBackwards, LeftDirection, LeftSpeed)
    #GenMotorControlSafetyNet(pwmRightMotorForwards, pwmRightMotorBackwards, RightDirection, RightSpeed)
    #time to wait after issuing motor commands
    time.sleep(waitTime)

def GenMotorControlSafetyNet(pwmMotorForwards, pwmMotorBackwards, Direction, Speed):
    if Direction == "Forwards":
        pwmMotorForwards.ChangeDutyCycle(Speed)
        pwmMotorBackwards.ChangeDutyCycle(DutyCycleStop)
    elif Direction == "Backwards":
        pwmMotorForwards.ChangeDutyCycle(DutyCycleStop)
        pwmMotorBackwards.ChangeDutyCycle(Speed)
    else:
        pwmMotorForwards.ChangeDutyCycle(DutyCycleStop)
        pwmMotorBackwards.ChangeDutyCycle(DutyCycleStop)

# Turn all motors off
def StopAll():
    print("Stopping motors!")
    GenMotorControl(Stp, DutyCycleStop, Stp, DutyCycleStop, 0)

# Turn both motors forwards
def Forwards(t):
    print("Forwards")
    GenMotorControl(Fwd, DutyCycleHigh, Fwd, DutyCycleHigh, t)

# Turn both motors backwards
def Backwards(t):
    print("Backwards")
    GenMotorControl(Bwd, DutyCycleHigh, Bwd, DutyCycleHigh, t)

# Turn Left going forward
def LeftForwards(t):
    print("Left Forwards")
    GenMotorControl(Fwd, DutyCycleLow, Fwd, DutyCycleHigh, t)

#Turn Left going backword 
def LeftBackwards(t):
    print("Left Backwards")
    GenMotorControl(Bwd, DutyCycleLow, Bwd, DutyCycleHigh, t)

# Turn Right going forward
def RightForwards(t):
    print("Right Forwards")
    GenMotorControl(Fwd, DutyCycleHigh, Fwd, DutyCycleLow, t)

# Turn Right going backward
def RightBackwards(t):
    print("Right Backwards")
    GenMotorControl(Bwd, DutyCycleHigh, Bwd, DutyCycleLow, t)
    
# Pivot Left
def PivotLeft(t):
    print("Pivot Left")
    GenMotorControl(Bwd, DutyCycleHigh, Fwd, DutyCycleHigh, t)

# Pivot Right
def PivotRight(t):
    print("Pivot Right")
    GenMotorControl(Fwd, DutyCycleHigh, Bwd, DutyCycleHigh, t)

# Left only Forward
def LeftOnlyForwards(t):
    print("Left Only Forward")
    GenMotorControl(Fwd, DutyCycleHigh, Stp, DutyCycleStop, t)

# Right Only Forward
def RightOnlyForwards(t):
    print("Right Only Forward")
    GenMotorControl(Stp, DutyCycleStop, Fwd, DutyCycleHigh, t)

# Left only Backward
def LeftOnlyBackwards(t):
    print("Left Only Backward")
    GenMotorControl(Bwd, DutyCycleHigh, Stp, DutyCycleStop, t)

# Right Only Backward
def RightOnlyBackwards(t):
    print("Right Only Backward")
    GenMotorControl(Stp, DutyCycleStop, Bwd, DutyCycleHigh, t)

# Exit the script cleanly
def ExitCleanly():
    StopAll()
    print("Cleaning up GPIO pins")
    GPIO.cleanup()
    print("Issue exit command")
    sys.exit()


# Your code to control the robot goes below this line
def Demo():
    key_control("W",1)
    key_control("A",1)
    key_control("D",1)
    key_control("X",0.3)
    key_control("E",1)
    key_control("W",1)
    key_control("Z",1)
    key_control("W",1)
    key_control("Q",3)
    ExitCleanly()

def printUsage():
    print("Enter a key followed by enter")
    print("W = Forwards")
    print("A = Left Forwards")
    print("S = Backwards")
    print("D = Right Forwards")
    print("Q = Pivot Left")
    print("P = Pivot Right")
    print("Z = Left Backwards")
    print("X = Stop")
    print("C = Right Backwards")
    print("H = Left Forwardsa Only")
    print("J = Left Backwards Only")
    print("K = Right Forwards Only")
    print("L = Right Backwards Only")
    print("\n")
    print("P = Demo")
    print("M = Exit")
    print("\n")


#input key from keyboard, appropriate action performed
def key_control(char, slptm):
    print "Key: ", char
    if char == 'W':
        Forwards(slptm)
    elif char == 'S':
        Backwards(slptm)
    elif char == 'A':
        LeftForwards(slptm)
    elif char == 'D':
        RightForwards(slptm)
    elif char == 'Z':
        LeftBackwards(slptm)
    elif char == 'C':
        RightBackwards(slptm)
    elif char == 'Q':
        PivotLeft(slptm)
    elif char == 'E':
        PivotRight(slptm)
    elif char == 'H':
        LeftOnlyBackwards(slptm)
    elif char == 'J':
        LeftOnlyForwards(slptm)
    elif char == 'K':
        RightOnlyForwards(slptm)
    elif char == 'L':
        RightOnlyBackwards(slptm)
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
    #command.bind('<KeyPress>', key_control)
    #command.mainloop()
    slptm=0.05
    printUsage()
    while True:
       try:
           input = raw_input("")
           key_control(input.upper(), slptm)
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
          time.sleep(slptm)

if __name__ == "__main__":
    main()
