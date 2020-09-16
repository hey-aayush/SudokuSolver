import cv2
import numpy as np

def Sudokugrid(Sudoku_image):
    image_copy=Sudoku_image
    grid_side_length=image_copy.shape[0]
    gray_image = cv2.cvtColor(image_copy, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray_image, (5,5), 0)
    _, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_OTSU)
    ret,thresh2 = cv2.threshold(th3, 127, 255, cv2.THRESH_BINARY_INV)
    return thresh2