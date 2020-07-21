# !/usr/bin/python3
# coding: utf-8

# Created by iagsoncarlos on Tuesday, June 16, 2020.
# Copyright (c) 2020 @iagsoncarlos. All rights reserved.

# --------------------------------------------------------------------------

def createArray(n):
    '''
    * createArray: Create an empty Array *

    Parameters:
        n: Number of positions in the array. (Type: Integer)
    Returns:
        arr: Returns an array with n positions. (Type: List)
    '''
    arr = [None] * n
    return arr

def fillArray(arr):
    '''
    * fillArray: Fill an Array *

    Parameters:
        arr: Enter an array. (Type: List)
    Returns:
        new: Returns a new array with the positions filled by the user. (Type: List)
    '''
    new = arr
    for i in range(len(arr)):
        new[i] = int(input('Enter the value of position {}: '.format(i)))

    return new

def readArray(arr):
    '''
    * readArray: Read each position of the Array *

    Parameters:
        arr: Enter an array. (Type: List)
    Returns:
        Returns showing the array.
    '''
    for i in range(len(arr)):
        print('Array [{}]: {}'.format(i, arr[i]))

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
    arr = createArray(10)
    arr = fillArray(arr)
    readArray(arr)

    # iH, vH = hl(1,arr)
    # print('\nIndex: {}, Higher Value: {}'.format(iH, vH))

    # iL, vL = hl(2, arr)
    # print('\nIndex: {}, Lowest Value: {}'.format(iL, vL))

    iH2, vH2, iL2, vL2 = hl(3, arr)
    print('\nIndex: {}, Higher Value: {}'.format(iH2, vH2))
    print('Index: {}, Lowest Value: {}'.format(iL2, vL2))
    print('Difference between the largest and the smallest: {}'.format(vH2-vL2))

if __name__ == "__main__":
    main()
