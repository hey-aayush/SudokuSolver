import cv2
import numpy as np

def return_grid_image(grid,return_size):
    side_length = return_size[0]//9
    grid_image= np.ones(return_size)
    for i in range(9):
        for j in range(9):
            grid_image=cv2.putText(grid_image,str(int(grid[j][i])),((side_length+1)*(i),(side_length-1)*(j+1)),cv2.FONT_HERSHEY_SIMPLEX ,0.7,(0,255,0),1)
    
    return grid_image  

def Display_grid(image,grid_image,sorted_points,grid_side):
    points_B = np.float32([[0,0], [grid_side,0], [0,grid_side], [grid_side,grid_side]])
    M = cv2.getPerspectiveTransform(points_B,sorted_points)
    warped = cv2.warpPerspective(grid_image, M, (640,480))
    result = (warped+image)/255
    return result