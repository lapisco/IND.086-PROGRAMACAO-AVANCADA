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

def elementMatrix(op, arr):
    '''
    * elementMatrix: Operation between the elements of the matrix itself. *

    Parameters:
        op: The operation you want to perform between the elements. (Type: Integer)
            If op = 1: Addition
            If op = 2: Subtraction
            If op = 3: Multiplication
            If op = 4: Division
        arr: Enter an Matrix. (Type: List)
    Returns:
        Returns a Integers or floats number with the result of the performed operations,-
        -or returns a message informed invalid operation, returning zero.

        return temp (Type: Integer or Float)
        return 0 (Type: Integer)
    '''
    rows = len(arr)
    cols = len(arr[0])

    temp = 0
    if op == 1:
        for i in range(rows):
            row = []
            for j in arr[i]:
                temp += j
        return temp

    elif op == 2:
        for i in range(rows):
            row = []
            for j in arr[i]:
                temp -= j
        return temp

    elif op == 3:
        temp = arr[0][0]
        cont = 0
        for i in range(rows):
            for j in arr[i]:
                if cont == 0:
                    temp = arr[0][0]
                    cont += 1
                else:
                    temp *= j
        return temp

    elif op == 4:
        temp = arr[0][0]
        cont = 0
        for i in range(rows):
            for j in arr[i]:
                if cont == 0:
                    temp = arr[0][0]
                    cont += 1
                else:
                    temp /= j
        return temp

    else:
        print('Invalid parameters, please read the documentation.')
        return 0

def main():
    arr = createMatrix(2, 3)
    aux = fillMatrix(arr)
    # readMatrix(aux)
    temp = elementMatrix(1, aux)
    print('\nSum between the elements of the matrix itself: ', temp)

if __name__ == "__main__":
    main()
