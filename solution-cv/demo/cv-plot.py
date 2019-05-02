# This module is used only to test the functionality
# of the camera and the color change property of the
# solution.

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import statistics
import time

cap = cv.VideoCapture(0)

# default value: plot 2s for quick test
times = 100

# h_mean = []
# s_mean = []
# v_mean = []

counter = -1
initial_time = time.time()
# ts = []

# area = []

isFristTime = True
isAfterFirstTime = False

START_THRESHOLD = 0.2
END_THRESHOLD = 0.05
INTERVAL = 1

while cap.isOpened():
    # Take each frame
    _, frame = cap.read()
    
    (height, width, channels) = frame.shape

    frame = cv.resize(frame, (int(height / 2), int(width / 2)))
    
    (height, width, channels) = frame.shape
    
    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([150, 255, 255])

    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    blue_black = cv.bitwise_and(frame, frame, mask=mask)
    # print(blue_black)

    # cv.imshow('frame', frame)
    # cv.imshow('mask', mask)
    # cv.imshow('blue black', blue_black)


    # filter out the black area
    # for each pixel
    #print(blue_black.shape)
    

    
    # collect points about every 4 secs considering the computational time
    if time.time() - initial_time > counter:
        counter += INTERVAL
        # print(counter)
        

        # find the blue area in the photo
        # h_list = []
        # s_list = []
        # v_list = []
        h_count = 0
        for i in range(0, height):
            for j in range(0, width):
                h = blue_black[i, j, 0]
                # s = blue_black[i, j, 1]
                # v = blue_black[i, j, 2]
                #print(h, s, v)
                if h: #not(h == 0 and s == 0 and v == 0):
                                #if h:
                    # h_list.append(h)
                    # s_list.append(s)
                    # v_list.append(v)
                    h_count += 1

        area_percent = h_count / (width * height)
        print('Area Percentage: ', area_percent)

        if isFristTime:
            # if re
            if area_percent > START_THRESHOLD:
                print('Bottle Detected')
                isFristTime = False
                isAfterFirstTime = True

        else:
            if area_percent < END_THRESHOLD:
                print('Reaciton Time: ', time.time() - initial_time)
                break

            if isAfterFirstTime:
                print('Timer Starts')
                initial_time = time.time()
                isAfterFirstTime = False

            # ts.append(time.time() - initial_time)
            # area.append(area_percent)
            # print('h_list', h_list,'s_list', s_list, 'v_list', v_list)

                # for each blue pixel, find the 
                # calculate mean(hsv)
            # if (len(h_list) and len(s_list) and len(v_list)):
            #   h_mean.append(statistics.mean(h_list))
            #   s_mean.append(statistics.mean(s_list))
            #   v_mean.append(statistics.mean(v_list))
            # else:
            #   h_mean.append(0)
            #   s_mean.append(0)
            #   v_mean.append(0)

    # if counter >= times - 1:
        # break

    if cv.waitKey(5) & 0xFF == ord('q'):
        break

    
# plot time - mean(hsv)
# plt.figure(1)
# plt.title('time - hsv')
# plt.plot(ts, h_mean, ts, s_mean, ts, v_mean)
# plt.xlabel('time/secs')
# plt.ylabel('color channel tensity')
# plt.legend(['h', 's', 'v'])


# plt.figure(2)
# plt.title('hsv - area(percentage)')
# plt.plot(ts, area)
# plt.xlabel('time/secs')
# plt.ylabel('area/percentage')
# plt.show()



while True:
    if cv.waitKey(5) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
