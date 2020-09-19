import cv2
import numpy as np
import SudokuSolve.WebCamExtract
import SudokuSolve.SudokuGrid
import SudokuSolve.ImageCrop
import SudokuSolve.ModelPredict
import SudokuSolve.DisplaySudoku
import SudokuSolve.GridSolve
from tensorflow.keras.models import load_model

def result(image,model):
    output_grid_size = (252,252)
    
    Grid_side = output_grid_size[0]

    processed_img=SudokuSolve.WebCamExtract.process_raw(image)

    approx = SudokuSolve.WebCamExtract.return_contours(processed_img)

    Sudoku_grid= np.zeros(output_grid_size)

    if len(approx)==4:
        sorted_points = SudokuSolve.WebCamExtract.sort_approx(approx)
        cv2.drawContours(image, [approx], 0, (0,0,0), 1)
        Sudoku_grid= SudokuSolve.WebCamExtract.Extract_sudoko(sorted_points,image,Grid_side,output_grid_size)
        processed_grid=SudokuSolve.SudokuGrid.Sudokugrid(Sudoku_grid)
        Predicted_grid=SudokuSolve.ModelPredict.modelPredictGrid(processed_grid,model)
        if SudokuSolve.GridSolve.isValidGrid(Predicted_grid):
            print("Valid Grid Found !!!")
            SudokuSolve.GridSolve.solve(Predicted_grid)
    
        grid_image = SudokuSolve.DisplaySudoku.return_grid_image(Predicted_grid,(output_grid_size[0],output_grid_size[0],3))
        result = SudokuSolve.DisplaySudoku.Display_grid(image,grid_image,sorted_points,Grid_side)
        return result
    return image