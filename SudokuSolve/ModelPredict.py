import cv2
import ImageCrop
import numpy as np

from tensorflow.keras.models import load_model

#add something like ki agr prediction accuracy km h to opening and erosion and dilation kre!!!

def modelPredictGrid(image,model):

    grid = np.array(np.zeros((9,9)))
    
    tst = []

    for i in range(9):
        for j in range(9):
            img_croped=ImageCrop.img_crop(i,j,image)
            img=cv2.resize(img_croped,(28,28))
            tst.append((1-img/255))
            
    tst_img=np.array(tst).reshape(81,28,28,1)
    grid_array = model.predict_classes(tst_img,batch_size=81,verbose=0)
    
    for i in range(9):
        for j in range(9):
            grid[i][j]=grid_array[9*i+j]
    
    #print(grid)
    return grid