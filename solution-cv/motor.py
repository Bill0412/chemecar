## motor.py
## class: Motor
# This module is used to control the motor
# by using a 5V voltage controled trigger 
# connected to the Raspberry Pi


from RPi.GPIO import *

class Motor:
	def __init__(self):
		setmode(BCM)

		self.trigger = 15

		setup(self.trigger, OUT)

	def move(self):
		output(self.trigger, HIGH)

	def stop(self):
		output(self.trigger, LOW)
