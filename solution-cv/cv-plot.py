import cv2 as cv

cap = cv.VideoCapture(0)

while cap.isOpened():
	_, frame = cap.read()

	
