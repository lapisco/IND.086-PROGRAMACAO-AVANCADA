# !/usr/bin/python3
# coding: utf-8

# Created by iagsoncarlos on Tuesday, June 16, 2020.
# Copyright (c) 2020 @iagsoncarlos. All rights reserved.

# --------------------------------------------------------------------------

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

def main():
    '''
    Calculate and print on the screen a 10x10 size matrix, in which its elements are in the form:
    A[i][j] = 2i + 7j – 2 se i < j
    A[i][j] = 3i2 - 1 se i = j
    A[i][j] = 4i3 + 5j2 + 1 se i > j
    '''
    rows = cols = 10

    arr = []
    for i in range(rows):
        row = []
        for j in range(cols):
            if i < j:
                temp = (2 * i + 7 * j - 2)
            elif i == j:
                temp = (3 * i * 2 - 1)
            elif i > j:
                temp = (4 * i * 3 + 5 * j * 2 + 1)
            row.append(temp)
        arr.append(row)
    readMatrix(arr)

if __name__ == "__main__":
    main()