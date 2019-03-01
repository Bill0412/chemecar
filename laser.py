import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
# singal for starting laser
GPIO.setup(18, GPIO.OUT)

try:
	while True:
		# the laser is alsways on
		GPIO.output(18, GPIO.HIGH)

		data = GPIO.input(23)
		print(data)
		

except KeyboardInterrupt: 
	GPIO.cleanup()
