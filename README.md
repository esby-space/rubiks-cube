# rubik's cube solver [°-°]

a webcam based rubik's cube solver!

## to calibrate

because every picture of a rubik's cube is different (lighting, color, shades, etc) calibration needs to be done before using it.  thank you so much to [nathancy](https://stackoverflow.com/questions/24916870/python-opencv-rubiks-cube-solver-color-extraction) for creating the ui!!

1. take a picture of the rubik's cube in your lighting
2. rename it `rubik.jpg` and put it in the `calibration` directory
3. run `python3 calibration/color_set.py`, adjust values until only the desired color can be seen
4. copy the numbers in the terminal into the `color.py` next to the calibrated color
5. repeat for all the colors in the

## to run

1. run `main.py`
2. align rubik's cube with the squares on screen
3. press space bar
4. (need to implement the rest of it >_>)

### dependencies
numpy, opencv, and kociemba

`pip install numpy opencv-python kociemba`
