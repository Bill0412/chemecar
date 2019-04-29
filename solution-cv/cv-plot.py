import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import statistics
import time

cap = cv.VideoCapture(0)

# default value: plot 2s for quick test
times = 100

h_mean = []
s_mean = []
v_mean = []

counter = -1
initial_time = time.time()
t = []

while cap.isOpened():
	# Take each frame
	_, frame = cap.read()
	frame = cv.flip(frame, 1)

	# Convert BGR to HSV
	hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

	# define range of blue color in HSV
	lower_blue = np.array([110, 50, 50])
	upper_blue = np.array([130, 255, 255])

	# Threshold the HSV image to get only blue colors
	mask = cv.inRange(hsv, lower_blue, upper_blue)

	# Bitwise-AND mask and original image
	blue_black = cv.bitwise_and(frame, frame, mask=mask)

	cv.imshow('frame', frame)
	cv.imshow('mask', mask)
	cv.imshow('bluck black', blue_black)


	# filter out the black area
	# for each pixel
	print(blue_black.shape)
	(height, width, channels) = blue_black.shape

	h_list = []
	s_list = []
	v_list = []
	for i in range(0, height):
		for j in range(0, width):
			h = blue_black[i, j, 0]
			s = blue_black[i, j, 1]
			v = blue_black[i, j, 2]

			if not(h == 0 and s == 0 and v == 0):
				h_list.append(h)
				s_list.append(s)
				v_list.append(v)

	# for each blue pixel, find the 
	# calculate mean(hsv)
	h_mean.append(statistics.mean(h_list))
	s_mean.append(statistics.mean(s_list))
	v_mean.append(statistics.mean(v_list))

	if time.time() - initial_time > counter:
		counter += 1
		t.append(counter)

	if counter >= times - 1:
		break

	
# plot time - mean(hsv)
plt.plot(t, h_mean, t, s_mean, t, v_mean)
plt.xlabel('time/secs')
plt.ylabel('color channel tensity')
plt.legend(['h', 's', 'v'])
plt.show()


while True:
	if cv.waitKey(5) & 0xFF == ord('q'):
		break

cap.release()
cv.destroyAllWindows()