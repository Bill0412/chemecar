# timer.py
# This module uses the camera to monitor the reaction process, when the reactions ends,
# it basically makes the whole program sleep until the reaction ends

import cv2 as cv
import numpy as np

class Timer:
	def __init__(self):
		self.cap = VideoCapture(0)

		## CONSTANTS
		self.area_start_threshold = 0.2
		self.area_end_threshold = 0.05
		self.image_shrink_ratio = 2

		# adjust the h value to adjust the color shreshold
		self.lower_blue = np.array([90, 50, 50])
		self.upper_blue = np.array([150, 255, 255])


		## Gloabal Varialbes
		self.image_height = None
		self.image_width = None
		self.image_area = None
		

	# get the blue-black image
	def __get_blue_black(self):
		_, frame = self.cap.read()

		(height, width, channels) = frame.shape

		# shrink the image to make it faster
		frame = cv.resize(frame, int(height / self.image_shrink_ratio), 
			int(width / self.image_shrink_ratio))

		if not self.image_height:
			(self.image_height, self.image_width, channels) = frame.shape
			self.image_area = self.image_height * self.image_width

		# convert BGR to HSV
		hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

		# Threshold the HSV image to get only blue colors
		mask = cv.inRange(hsv, lower_blue, upper_blue)

		# Bitwise-AND mask and original image
		# and return the blue-black image
		return cv.bitwise_and(frame, frame, mask=mask)

	def __get_area_percentage(self):

		# get the blue-black image
		blue_black = self.__get_blue_black()

		count = 0

		for i in range(0, self.image_height):
			for j in range(0, self.image_width):
				h = blue_black[i, j, 0]

				# if it's blue area
				if h:
					h_count += 1

		return count / self.image_area

	# This function waits until the solution is in place
	# Finishing this function is the prerequisite for 
	# starting the motor
	def wait_solution(self):
		while True:
			if self.__get_area_percentage() > self.area_start_threshold:
				break

			# Cautious: this might fail
			cv.waitKey(5)



	# This function contains a loop that continuously checks
	# if the reaction has termintated, if it is terminated,
	# The function should return.
	def timing_reaciton(self):
		while True:
			# if the color fades almost totally
			if self.__get_area_percentage() < self.area_end_threshold:
				break

			# Cautious: this might fail
			cv.waitKey(5)







	


