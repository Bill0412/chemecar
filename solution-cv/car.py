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

    def start_competition(self):
        
        
        # if blue is detected, move the motor, and 
        self.timer.wait_solution(self.motor.light_on, self.motor.light_off)

        # start the car
        self.motor.move()

        # wait for the timing reaction
        self.timer.timing_reaction()

        # when the reaction ends, stop the car
        self.motor.stop()


if __name__ == '__main__':
    car = Car()
    car.start_competition()