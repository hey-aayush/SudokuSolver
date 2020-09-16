import cv2
import numpy as np
import WebCamExtract
import SudokuGrid
import ImageCrop
import ModelPredict
import DisplaySudoku
from tensorflow.keras.models import load_model

def result(image,model):
    output_grid_size = (252,252)
    
    Grid_side = output_grid_size[0]

    processed_img=WebCamExtract.process_raw(image)

    approx = WebCamExtract.return_contours(processed_img)

    Sudoku_grid= np.zeros(output_grid_size)

    if len(approx)==4:
        sorted_points = WebCamExtract.sort_approx(approx)
        cv2.drawContours(image, [approx], 0, (0,0,0), 1)
        Sudoku_grid= WebCamExtract.Extract_sudoko(sorted_points,image,Grid_side,output_grid_size)
        processed_grid=SudokuGrid.Sudokugrid(Sudoku_grid)
        Predicted_grid=ModelPredict.modelPredictGrid(processed_grid,model)
        grid_image = DisplaySudoku.return_grid_image(Predicted_grid,(output_grid_size[0],output_grid_size[0],3))
        result = DisplaySudoku.Display_grid(image,grid_image,sorted_points,Grid_side)
        return result
    return image
