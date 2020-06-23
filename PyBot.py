import RPi.GPIO as GPIO
from time import sleep

class PyBot:
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
	
	def __init__(self):
		GPIO.setmode(GPIO.BOARD)
		GPIO.setwarnings(False)
		GPIO.setup(PyBot.LeftFrontA,GPIO.OUT)
		GPIO.setup(PyBot.LeftFrontB,GPIO.OUT)
		GPIO.setup(PyBot.LeftFrontE,GPIO.OUT)

		GPIO.setup(PyBot.RightFrontA,GPIO.OUT)
		GPIO.setup(PyBot.RightFrontB,GPIO.OUT)
		GPIO.setup(PyBot.RightFrontE,GPIO.OUT)

		GPIO.setup(PyBot.LeftRearA,GPIO.OUT)
		GPIO.setup(PyBot.LeftRearB,GPIO.OUT)
		GPIO.setup(PyBot.LeftRearE,GPIO.OUT)

		GPIO.setup(PyBot.RightRearA,GPIO.OUT)
		GPIO.setup(PyBot.RightRearB,GPIO.OUT)
		GPIO.setup(PyBot.RightRearE,GPIO.OUT)
		self.stop()

	def forward(self):
		GPIO.output(PyBot.LeftFrontA,GPIO.HIGH)
		GPIO.output(PyBot.LeftFrontB,GPIO.LOW)
		GPIO.output(PyBot.LeftFrontE,GPIO.HIGH)

		GPIO.output(PyBot.LeftRearA,GPIO.HIGH)
		GPIO.output(PyBot.LeftRearB,GPIO.LOW)
		GPIO.output(PyBot.LeftRearE,GPIO.HIGH)

		GPIO.output(PyBot.RightFrontA,GPIO.HIGH)
		GPIO.output(PyBot.RightFrontB,GPIO.LOW)
		GPIO.output(PyBot.RightFrontE,GPIO.HIGH)

		GPIO.output(PyBot.RightRearA,GPIO.HIGH)
		GPIO.output(PyBot.RightRearB,GPIO.LOW)
		GPIO.output(PyBot.RightRearE,GPIO.HIGH)
		sleep(2)
		self.stop()

	def backward(self):
		GPIO.output(PyBot.LeftFrontA,GPIO.LOW)
		GPIO.output(PyBot.LeftFrontB,GPIO.HIGH)
		GPIO.output(PyBot.LeftFrontE,GPIO.HIGH)

		GPIO.output(PyBot.LeftRearA,GPIO.LOW)
		GPIO.output(PyBot.LeftRearB,GPIO.HIGH)
		GPIO.output(PyBot.LeftRearE,GPIO.HIGH)

		GPIO.output(PyBot.RightFrontA,GPIO.LOW)
		GPIO.output(PyBot.RightFrontB,GPIO.HIGH)
		GPIO.output(PyBot.RightFrontE,GPIO.HIGH)

		GPIO.output(PyBot.RightRearA,GPIO.LOW)
		GPIO.output(PyBot.RightRearB,GPIO.HIGH)
		GPIO.output(PyBot.RightRearE,GPIO.HIGH)
		sleep(2)
		self.stop()
	
	def right(self):
		GPIO.output(PyBot.LeftFrontA,GPIO.HIGH)
		GPIO.output(PyBot.LeftFrontB,GPIO.LOW)
		GPIO.output(PyBot.LeftFrontE,GPIO.HIGH)

		GPIO.output(PyBot.LeftRearA,GPIO.HIGH)
		GPIO.output(PyBot.LeftRearB,GPIO.LOW)
		GPIO.output(PyBot.LeftRearE,GPIO.HIGH)


		GPIO.output(PyBot.RightFrontA,GPIO.LOW)
		GPIO.output(PyBot.RightFrontB,GPIO.HIGH)
		GPIO.output(PyBot.RightFrontE,GPIO.HIGH)

		GPIO.output(PyBot.RightRearA,GPIO.LOW)
		GPIO.output(PyBot.RightRearB,GPIO.HIGH)
		GPIO.output(PyBot.RightRearE,GPIO.HIGH)
		sleep(2)
		self.stop()

	def left(self):
		GPIO.output(PyBot.LeftFrontA,GPIO.LOW)
		GPIO.output(PyBot.LeftFrontB,GPIO.HIGH)
		GPIO.output(PyBot.LeftFrontE,GPIO.HIGH)

		GPIO.output(PyBot.LeftRearA,GPIO.LOW)
		GPIO.output(PyBot.LeftRearB,GPIO.HIGH)
		GPIO.output(PyBot.LeftRearE,GPIO.HIGH)
		
		GPIO.output(PyBot.RightFrontA,GPIO.HIGH)
		GPIO.output(PyBot.RightFrontB,GPIO.LOW)
		GPIO.output(PyBot.RightFrontE,GPIO.HIGH)

		GPIO.output(PyBot.RightRearA,GPIO.HIGH)
		GPIO.output(PyBot.RightRearB,GPIO.LOW)
		GPIO.output(PyBot.RightRearE,GPIO.HIGH)
		sleep(2)
		self.stop()
	
	def stop(self):
		GPIO.output(PyBot.LeftFrontE,GPIO.LOW)
		GPIO.output(PyBot.RightFrontE,GPIO.LOW)
		GPIO.output(PyBot.LeftRearE,GPIO.LOW)
		GPIO.output(PyBot.RightRearE,GPIO.LOW)
	
	def shutdown(self):
		self.stop()
		GPIO.cleanup()
