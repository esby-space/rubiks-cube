from typing import Tuple
import kociemba as kc
import cv2 as cv
import numpy as np
import math

from color import colors


def main() -> None:
    # initialize opencv frame
    cam = cv.VideoCapture(0)
    ret, img = cam.read()

    # calculate coordinates of cube overlay
    margin = 100
    length = img.shape[0] - (2 * margin)
    start_point = (math.floor((img.shape[1] - length) / 2), margin)
    end_point = (math.floor((img.shape[1] + length) / 2), img.shape[0] - margin)

    # main loop
    while True:
        ret, img = cam.read()
        if not ret:
            raise Exception("couldn't grab the frame x_x")
            break

        k = cv.waitKey(1)
        if k % 256 == 27:
            # ESC pressed
            print("closing the program")
            break

        if k % 256 == 32:
            # SPACE pressed
            get_color(img, start_point, end_point)

        img = draw_cube(img, start_point, end_point)
        cv.imshow("esby rubik's cube solver :D", img)

    # close everything
    cam.release()
    cv.destroyAllWindows()


def draw_cube(img, start: Tuple[int, int], end: Tuple[int, int]):
    """draws a cube overlay into the image"""

    start_x, start_y = start
    end_x, end_y = end
    dif_x = math.ceil((end_x - start_x) / 3)
    dif_y = math.ceil((end_y - start_y) / 3)

    for i in range(start_x, end_x + dif_x, dif_x):
        img = cv.line(img, (i, start_y), (i, end_y), (0, 0, 0), 2)
    for i in range(start_y, end_y + dif_y, dif_y):
        img = cv.line(img, (start_x, i), (end_x, i), (0, 0, 0), 2)

    return img


def get_color(img, start: Tuple[int, int], end: Tuple[int, int]):
    """Get rubik's cube color from given image"""
    start_x, start_y = start
    end_x, end_y = end
    img = img[start_y:end_y, start_x:end_x]

    cv.imshow("og", img)
    hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    for color in colors:
        lower = np.array(colors[color][0], np.uint8)
        upper = np.array(colors[color][1], np.uint8)
        threshold = cv.inRange(hsv_img, lower, upper)
        cv.imshow(color, threshold)


if __name__ == "__main__":
    main()
