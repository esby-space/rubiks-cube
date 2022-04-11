from typing import Tuple, Dict
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

    # cube variables!
    cube_string = ""

    # main loop
    while True:
        ret, img = cam.read()

        k = cv.waitKey(1)
        if k % 256 == 27:
            # ESC pressed
            print("closing the program")
            break

        if k % 256 == 32:
            # SPACE pressed
            cube_string += get_face_colors(img, start_point, end_point)
            prompt(math.floor(len(cube_string) / 9), cube_string)

            if len(cube_string) == 54:
                print(kc.solve(cube_string))

        img = draw_grid(img, start_point, end_point)
        cv.imshow("esby rubik's cube solver :D", img)

    # close everything
    cam.release()
    cv.destroyAllWindows()


def get_face_colors(img, start: Tuple[int, int], end: Tuple[int, int]) -> str:
    """Gets all the colors from a face of the rubik's cube"""
    start_x, start_y = start
    end_x, end_y = end
    dif_x = math.ceil((end_x - start_x) / 3)
    dif_y = math.ceil((end_y - start_y) / 3)

    color_string = ""
    # iterate over all the squares in the rubik's face
    for i in range(start_y, end_y, dif_y):
        for j in range(start_x, end_x, dif_x):
            # only get the main color of one square on the face
            square = img[i : i + dif_y, j : j + dif_x]
            color_symbol = get_color(square)[0].upper()
            color_string += color_symbol

    return color_string


def get_color(img) -> str:
    """Gets an images main color from a given image"""
    color_values = get_color_values(img)
    main_color: None | str = None
    largest_value = 0

    for color, value in color_values.items():
        if value > largest_value:
            main_color = color
            largest_value = value

    if main_color is None:
        main_color = "none"

    return main_color


def get_color_values(img) -> Dict[str, int]:
    """Gets the color from a given image"""
    # image filtering idk
    img = cv.bilateralFilter(img, 9, 75, 75)
    img = cv.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)

    # convert to hsv, works better for color thresholds
    hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    color_values: Dict[str, int] = {}

    for color in colors:
        lower = np.array(colors[color][0], np.uint8)
        upper = np.array(colors[color][1], np.uint8)
        threshold = cv.inRange(hsv_img, lower, upper)
        color_values[color] = threshold.sum()

    return color_values


def prompt(face_number: int, cube_string: str) -> None:
    print(
        f"""
        --- SCANNING FACE {face_number} / 6 ---
        Current cube string: {cube_string}
    """
    )


def draw_grid(img, start: Tuple[int, int], end: Tuple[int, int]):
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


if __name__ == "__main__":
    main()
