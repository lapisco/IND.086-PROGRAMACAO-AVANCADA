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

def diagonal(n, arr):
    '''
    * diagonal: Returns the diagonal of a Matrix *

    Parameters:
        n: It is an integer value that defines between main and/or secondary diagonal.
            n == 1: Main diagonal
            n == 2: Secondary diagonal
            n == 3: Main and Secondary diagonal (respectively).
            n == 4: Returns the matrix without the main diagonal.
            n == 5: Returns the matrix without the secondary diagonal.
            n == 6: Returns the matrix without the main and secondary diagonal. (Type: Integer)
        arr: Enter an Matrix. (Type: List)
    Returns:
        Returns an array with main or secondary, or both diagonals. (Type: List)
        Returns an array without main or secondary, or both diagonals. (Type: List)
    '''
    diagonal1 = []
    diagonal2 = []
    noDiagonal1 = []
    noDiagonal2 = []
    noDiagonal3 = []

    if n == 1:
        for i in range(len(arr)):
            diagonal1.append(arr[i][i])
        return diagonal1

    elif n == 2:
        for i in range(len(arr)):
            diagonal2.append(arr[i][len(arr)-1-i])
        return diagonal2

    elif n == 3:
        for i in range(len(arr)):
            diagonal1.append(arr[i][i])
            diagonal2.append(arr[i][len(arr)-1-i])
        return diagonal1, diagonal2

    elif n == 4:
        for i in range(len(arr)):
            for j in arr[i]:
                if j == arr[i][i]:
                    pass
                else:
                    noDiagonal1.append(j)
        return noDiagonal1

    elif n == 5:
        for i in range(len(arr)):
            for j in arr[i]:
                if j == (arr[i][len(arr)-1-i]):
                    pass
                else:
                    noDiagonal2.append(j)
        return noDiagonal2
    
    elif n == 6:
        for i in range(len(arr)):
            for j in arr[i]:
                if (j == arr[i][i]) or (j == (arr[i][len(arr)-1-i])):
                    pass
                else:
                    noDiagonal3.append(j)
        return noDiagonal3

    else:
        print('Invalid parameters, please read the documentation.')
        return 0
    
def main():
    arr = createMatrix(3, 3)
    aux = fillMatrix(arr)
    # readMatrix(aux)
    temp = diagonal(1, aux)
    print('This is the main diagonal of the matrix. ', temp)

if __name__ == "__main__":
    main()