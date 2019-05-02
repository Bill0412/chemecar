## Module Car
## This is the main module of this project.
# It observes the reaction of the solution and 
# controls the move and stop of the motors according
# to the timing reaction.


from motor import Motor
from timer import Timer

class Car:
	def __init__(self):
		self.timer = Timer()
		self.motor = Motor()

	def loop(self):
		
		# start the car (when to start?) 
		motor.move()

		# wait for the timing reaction
		timer.timing_reaction()

		# when the reaction ends, stop the car
		motor.stop()