import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BOARD)
 
LeftFrontA = 37
LeftFrontB = 35
LeftFrontE = 33

LeftRearA = 31
LeftRearB = 29
LeftRearE = 23
 
RightFrontA = 40
RightFrontB = 38
RightFrontE = 36

RightRearA = 32
RightRearB = 26
RightRearE = 24
 
GPIO.setup(LeftFrontA,GPIO.OUT)
GPIO.setup(LeftFrontB,GPIO.OUT)
GPIO.setup(LeftFrontE,GPIO.OUT)

GPIO.setup(RightFrontA,GPIO.OUT)
GPIO.setup(RightFrontB,GPIO.OUT)
GPIO.setup(RightFrontE,GPIO.OUT)

GPIO.setup(LeftRearA,GPIO.OUT)
GPIO.setup(LeftRearB,GPIO.OUT)
GPIO.setup(LeftRearE,GPIO.OUT)

GPIO.setup(RightRearA,GPIO.OUT)
GPIO.setup(RightRearB,GPIO.OUT)
GPIO.setup(RightRearE,GPIO.OUT)
 
print ("Turning motor on")
GPIO.output(LeftFrontA,GPIO.HIGH)
GPIO.output(LeftFrontB,GPIO.LOW)
GPIO.output(LeftFrontE,GPIO.HIGH)

GPIO.output(LeftRearA,GPIO.HIGH)
GPIO.output(LeftRearB,GPIO.LOW)
GPIO.output(LeftRearE,GPIO.HIGH)

GPIO.output(RightFrontA,GPIO.HIGH)
GPIO.output(RightFrontB,GPIO.LOW)
GPIO.output(RightFrontE,GPIO.HIGH)

GPIO.output(RightRearA,GPIO.HIGH)
GPIO.output(RightRearB,GPIO.LOW)
GPIO.output(RightRearE,GPIO.HIGH)
 
sleep(5)
 
print("Stopping motor")
GPIO.output(LeftFrontE,GPIO.LOW)
GPIO.output(RightFrontE,GPIO.LOW)
GPIO.output(LeftRearE,GPIO.LOW)
GPIO.output(RightRearE,GPIO.LOW)
 
GPIO.cleanup()
