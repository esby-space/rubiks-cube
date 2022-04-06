# importing required libraries
import cv2
import numpy as np

# taking the input from webcam
vid = cv2.VideoCapture(0)

# running while loop just to make sure that
# our program keep running untill we stop it
while True:

    # capturing the current frame
    _, frame = vid.read()

    # displaying the current frame
    cv2.imshow("frame", frame)

    # setting values for base colors
    r = frame[:, :, 2:]
    g = frame[:, :, 1:2]
    b = frame[:, :, :1]

    # computing the mean
    b_mean = np.mean(b)
    g_mean = np.mean(g)
    r_mean = np.mean(r)

    # displaying the most prominent color
    if b_mean > g_mean and b_mean > r_mean:
        print("Blue")
    if g_mean > r_mean and g_mean > b_mean:
        print("Green")
    if r_mean > g_mean and r_mean > b_mean:
        print("Red")
    else:
        print("idk")
