from RPi.GPIO import *

setmode(BCM)

Trigger = 15
# control the trigger
setup(Trigger, OUT)

try:
    while True:
        output(Trigger, LOW)
except:
    cleanup()
    
    



