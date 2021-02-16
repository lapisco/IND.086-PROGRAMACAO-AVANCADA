# !/usr/bin/python3
# coding: utf-8

# Created by iagsoncarlos on Tuesday, June 16, 2020.
# Copyright (c) 2020 @iagsoncarlos. All rights reserved.

# --------------------------------------------------------------------------

def createMatrix(rows, cols):
    '''
    * createMatrix: Create an empty Matrix *

    Parameters:
        rows: Number of rows. (Type: Integer)
        cols: Number of columns. (Type: Integer)
    Returns:
        arr: Returns a Matrix with rows x cols positions. (Type: List)
    '''
    arr = []
    for i in range(rows):
        row = []
        for j in range(cols):
            # temp = int(input('Add the value of arr[{}][{}]: '.format(i, j)))
            row.append(None)
        arr.append(row)
    return arr

def fillMatrix(arr):
    '''
    * createMatrix: Create an empty Matrix *

    Parameters:
        arr: Enter an Matrix. (Type: List)
    Returns:
        arr: Returns a user-filled matrix. (Type: List)
        return arr
    '''
    rows = len(arr)
    cols = len(arr[0])

    arr = []
    for i in range(rows):
        row = []
        for j in range(cols):
            temp = int(input('Add the value of arr[{}][{}]: '.format(i, j)))
            row.append(temp)
        arr.append(row)
    return arr

def main():
    aux = createMatrix(3, 3)
    arr = fillMatrix(aux)

    col_1 = []
    for i in arr:
        col_1.append(i[0])

    print('\nThe 1st col is: ', col_1)

if __name__ == "__main__":
    main()