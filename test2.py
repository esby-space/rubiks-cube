import cv2
import numpy as np

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k % 256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k % 256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

        r = frame[:, :, 2:]
        g = frame[:, :, 1:2]
        b = frame[:, :, :1]

        b_mean = np.mean(b)
        g_mean = np.mean(g)
        r_mean = np.mean(r)

        if b_mean > g_mean and b_mean > r_mean:
            print("Blue")
        elif g_mean > r_mean and g_mean > b_mean:
            print("Green")
        elif r_mean > g_mean and r_mean > b_mean:
            print("Red")
        else:
            print("idk")


cam.release()

cv2.destroyAllWindows()
