from typing import Tuple, Dict
import kociemba as kc
import cv2 as cv
import numpy as np
import math

from color import colors


def main():
    cam = cv.VideoCapture(0)
    ret, img = cam.read()

    while True:
        ret, img = cam.read()

        k = cv.waitKey(1)
        if k % 256 == 27:
            # ESC pressed
            print("closing the program")
            break

        if k % 256 == 32:
            # SPACE pressed
            img = cv.GaussianBlur(img, (5, 5), 0)
            cv.imshow("asdf", img)

        cv.imshow("esby rubik's cube solver :D", img)

    # close everything
    cam.release()
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()
