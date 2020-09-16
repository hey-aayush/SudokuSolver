import cv2
import numpy as np

def img_crop(i,j,image):
    side_length=image.shape[0]//9
    cropped_img = image[side_length*i:side_length*(i+1),side_length*j:side_length*(j+1)]
    return cropped_img