import numpy as np

def return_subSquare(x,y,grid):
    return grid[3*int(y/3):3*int(y/3)+3,3*int(x/3):3*int(x/3)+3]

def isPossible(y,x,n,grid):
    for i in range(0,9):
        if (grid[y][i]==n) and (i!=x):
            return False
    for i in range(0,9):
        if (grid[i][x]==n) and (i!=y):
            return False
    SubSquare = return_subSquare(x,y,grid)
    for i in range(0,3):
        for j in range(0,3):
            if SubSquare[i][j]==n and (i!=y and j!=x):
                return False
    return True

def Empty_box(grid):
    for i in range(0,9):
        for j in range(0,9):
            if grid[i][j]==0:
                   return (i,j)
    return None 

def solve(grid):
    if not Empty_box(grid):
        return True
    else:
        row,col = Empty_box(grid)
        for k in range(1,10):
            if isPossible(row,col,k,grid):
                grid[row][col]=k
                if solve(grid):
                    return True
                grid[row][col]=0
        return False

def isValidGrid(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j]!=0:
                if (not isPossible(i,j,grid[i][j],grid)):
                    return False
    return True