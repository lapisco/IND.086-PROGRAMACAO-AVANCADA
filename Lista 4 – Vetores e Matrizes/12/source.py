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

def hl(n, arr):
    '''
    * hl: Higher and Lower Value *

    Parameters:
        n: Defines the desired return by the function user.
           There are three possible returns:
                if n = 1 it returns the index and the highest value;
                if n = 2 it returns the index and the lowest value;
                if n = 3 it returns the index and the highest value,
                    and the index and the lowest value respectively. (Type: Integer)
        arr: Enter an array. (Type: List)
    Returns:
        n == 1: iMax, vMax (Type: Integer)
        n == 2: iMin, vMin (Type: Integer)
        n == 3: iMax, vMax, iMin, vMin (Type: Integer)
    Examples:
        iH, vH = hl(1,arr)
        iL, vL = hl(2, arr)
        iH2, vH2, iL2, vL2 = hl(3, arr)
    '''
    vMax = 0
    vMin = arr[0]
    iMax = 0
    iMin = 0

    if n == 1:
        for i in range(len(arr)):
            if vMax < arr[i]:
                vMax = arr[i]
                iMax = i
        return iMax, vMax

    elif n == 2:
        for i in range(len(arr)):
            if vMin > arr[i]:
                vMin  = arr[i]
                iMin = i
        return iMin, vMin

    elif n == 3:
        for i in range(len(arr)):
            if vMax < arr[i]:
                vMax = arr[i]
                iMax = i
            if vMin > arr[i]:
                vMin  = arr[i]
                iMin = i
        return iMax, vMax, iMin, vMin

    else:
        print('Invalid parameters, please read the documentation.')

def main():
    '''
    Read a 10x3 size matrix with the grades of 10 students in three tests.
    Then, calculate and write on the screen the number of students whose worst grade was in test 1,
    the number of students whose worst grade was in test 2
    and the number of students whose worst grade was in test 3.

    '''
    aux = createMatrix(10, 3)
    arr = fillMatrix(aux)

    l0 = l1 = l2 = 0
    h0 = h1 = h2 = 0

    for i in range(len(arr)):
        indexH, bigger, indexL, smaller = hl(3, arr[i])    
        print('Student {}: Bigger: {}, e Smaller: {}'.format(i, bigger, smaller))

        if indexL == 0:
            l0 += 1
        if indexL == 1:
            l1 += 1
        if indexL == 2:
            l2 += 1

        if indexH == 0:
            h0 += 1
        if indexH == 1:
            h1 += 1
        if indexH == 2:
            h2 += 1

    print('\nTest 1: Lowest grade: {}, and Highest grade: {}'.format(l0, h0))
    print('Test 2: Lowest grade: {}, and Highest grade: {}'.format(l1, h1))
    print('Test 3: Lowest grade: {}, and Highest grade: {}'.format(l2, h2))

if __name__ == "__main__":
    main()