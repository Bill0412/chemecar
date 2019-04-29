import RPi.GPIO as GPIO
# import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN)

try:
	while True:
		data = GPIO.input(18)
		print(data)

except KeyboardInterrupt: 
	GPIO.cleanup()
