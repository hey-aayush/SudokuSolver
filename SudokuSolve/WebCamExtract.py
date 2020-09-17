import cv2
import numpy as np

def process_raw(image):
    gray_img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    blur_gry=cv2.GaussianBlur(gray_img,(3,3),1)
    _, th3 = cv2.threshold(blur_gry, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    ret,thresh2 = cv2.threshold(th3, 127, 255, cv2.THRESH_BINARY_INV)

    return thresh2

def return_contours(processed):
    contours, hierarchy = cv2.findContours(processed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)
    for i in range(len(sorted_contours)):
        approx = cv2.approxPolyDP(sorted_contours[i], 0.01*cv2.arcLength(sorted_contours[i],True),True)
        if len(approx) == 4:
            return approx;
    return [1]

def sort_approx(approx):
    sorted_approx = sorted(approx,key=lambda k:[k[0][1],k[0][0]])
    sorted_approx[:2]= sorted(approx[0:2],key=lambda k:k[0][0])
    sorted_approx[2:4]= sorted(approx[2:4],key=lambda k:k[0][0])
    sorted_points=[] #pehele hi lst m convert krne hai !!
    for i in range(4):
        sorted_points.append(sorted_approx[i].tolist()[0])
    return np.float32(sorted_points)

def Extract_sudoko(sorted_points,image,grid_side,output_grid_size):
    points_B = np.float32([[0,0], [grid_side,0], [0,grid_side], [grid_side,grid_side]])
    M = cv2.getPerspectiveTransform(sorted_points, points_B)
    warped = cv2.warpPerspective(image, M, output_grid_size)
    return warped

def show_frames(image,output_grid_size):    

    grid_side = output_grid_size[0]
    processed_img=process_raw(image)
    approx = return_contours(processed_img)
    Sudoku_grid= np.zeros(output_grid_size)

    if len(approx)==4:
        sorted_points = sort_approx(approx)
        #cv2.drawContours(image, [approx], 0, (0,0,0), 5)
        Sudoku_grid= Extract_sudoko(sorted_points,image,grid_side,output_grid_size)

    return image,Sudoku_grid