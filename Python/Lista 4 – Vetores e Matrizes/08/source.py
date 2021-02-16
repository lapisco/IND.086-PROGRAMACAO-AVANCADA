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

def readMatrix(arr):
    '''
    * readMatrix: Read each position of the Matrix *

    Parameters:
        arr: Enter an Matrix. (Type: List)
    Returns:
        Returns showing the Matrix.
    '''
    for i in range(len(arr)):
        print(arr[i])

def mathMatrix(n, op, arr):
    '''
    * mathMatrix: Matrix element-by-element mathematical operations. *

    Parameters:
        n: The value you want to perform the element-by-element operation. (Type: Integer)
        op: The operation you want to perform element by element. (Type: Integer)
            If op = 1: Addition
            If op = 2: Subtraction
            If op = 3: Multiplication
            If op = 4: Division
        arr: Enter an Matrix. (Type: List)
    Returns:
        Returns a matrix with the result of the performed operations,-
        -or returns a message informed invalid operation, returning zero.

        return new (Type: List)
        return 0 (Type: Integer)
    Example:
        temp = mathMatrix(2, 1, arr)
        temp = mathMatrix(2, 2, arr)
        temp = mathMatrix(2, 3, arr)
        temp = mathMatrix(2, 4, arr)
    '''
    rows = len(arr)
    cols = len(arr[0])

    new = []
    if op == 1:
        for i in range(rows):
            row = []
            for j in arr[i]:
                row.append(j + n)
            new.append(row)
        return new

    elif op == 2:
        for i in range(rows):
            row = []
            for j in arr[i]:
                row.append(j - n)
            new.append(row)
        return new

    elif op == 3:
        for i in range(rows):
            row = []
            for j in arr[i]:
                row.append(j * n)
            new.append(row)
        return new

    elif op == 4:
        for i in range(rows):
            row = []
            for j in arr[i]:
                row.append(j / n)
            new.append(row)
        return new

    else:
        print('Invalid parameters, please read the documentation.')
        return 0

def main():
    arr = createMatrix(3, 3)
    aux = fillMatrix(arr)
    # readMatrix(aux)
    temp = mathMatrix(2, 3, aux)
    print('\n')
    readMatrix(temp)

if __name__ == "__main__":
    main()