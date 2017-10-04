#Import Libraries
import time
import RPi.GPIO as GPIO

#Set the GPIO Mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Set up the pins
PINLDR = 17
PINLEDRED = 22
PINLEDBLUE = 23
PINBUZZER = 27

#percentages for brightness control
#YOU MUST CHANGE THESE, REMEMBER THAT THE HIGHER THE NUMBER THE DARKER IT IS, CLOSER TO 0 THE BRIGHTER IT IS
REALLYBRIGHT=50
BRIGHT=500
DULL=1000

#LED pinds
GPIO.setup(PINLDR, GPIO.IN)
GPIO.setup(PINLEDRED, GPIO.OUT)
GPIO.setup(PINLEDBLUE, GPIO.OUT)
GPIO.setup(PINBUZZER, GPIO.OUT)

#read the brightness from the LDR
#higher numbers indicate darker conditions
def ReadLDR():
    LDRCount = 0 # Sets the count to 0
    GPIO.setup(PINLDR, GPIO.OUT)
    GPIO.output(PINLDR, GPIO.LOW)
    time.sleep(0.1) # Drains all charge from the capacitor
    GPIO.setup(PINLDR, GPIO.IN) # Sets the pin to be input
    # While the input pin reads 'off' or Low, count
    while (GPIO.input(PINLDR) == GPIO.LOW):
        LDRCount += 1 # Add one to the counter
    return LDRCount
  
while True:
    try:
        brightness = ReadLDR()
        GPIO.output(PINLEDRED, GPIO.LOW)  
        GPIO.output(PINLEDBLUE, GPIO.HIGH)
        GPIO.output(PINLEDBLUE, GPIO.LOW)
        print(brightness)
        if (brightness >= DULL):
            #this is dark, everything off
            GPIO.output(PINLEDRED, GPIO.LOW)
            GPIO.output(PINLEDBLUE, GPIO.LOW)
            GPIO.output(PINBUZZER, GPIO.LOW)
        elif (brightness < DULL and brightness >= BRIGHT):
            #this is dull, blue on
            GPIO.output(PINLEDRED, GPIO.LOW)
            GPIO.output(PINLEDBLUE, GPIO.HIGH)
            GPIO.output(PINBUZZER, GPIO.LOW)
        elif (brightness < BRIGHT and brightness >= REALLYBRIGHT):
            #this is bright, red on
            GPIO.output(PINLEDRED, GPIO.HIGH)
            GPIO.output(PINLEDBLUE, GPIO.LOW)
            GPIO.output(PINBUZZER, GPIO.LOW)
        elif (brightness <= REALLYBRIGHT):
            GPIO.output(PINLEDRED, GPIO.LOW)
            GPIO.output(PINLEDBLUE, GPIO.LOW)   
            GPIO.output(PINBUZZER, GPIO.HIGH)
        time.sleep(1)
    except:
      GPIO.cleanup()
