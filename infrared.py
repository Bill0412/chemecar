import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
# singal for starting laser
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.IN)

try:
	while True:
		# the infrared light is alsways on
		GPIO.output(18, GPIO.HIGH)

		data = GPIO.input(23)
		nZero = 0
		nOne = 0
		if data == 0:
			nZero++
		else:
			nOne++

		total = nZero + nOne
		
		if total == 1000:
			nZero = 0
			nOne = 0
		print( "detection rate: " + nZero/total, "missing rate: " + nOne/total, sep="; ")
		

except KeyboardInterrupt: 
	GPIO.cleanup()