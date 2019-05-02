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
        self.light = 14

        setup(self.trigger, OUT)
        setup(self.light, OUT)

    def light_on(self):
        output(self.light, HIGH)
        
    def light_off(self):
        output(self.light, LOW)
        
    def move(self):
        output(self.trigger, HIGH)

    def stop(self):
        output(self.trigger, LOW)
        cleanup()
