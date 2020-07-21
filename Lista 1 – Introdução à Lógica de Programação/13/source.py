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

def hls(n, arr, sm=False):
    '''
    * hls: Higher, Lower Value and Sum of the numbers. *

    Parameters:
        n: Defines the desired return by the function user.
           There are three possible returns:
                if n = 1 it returns the index and the highest value;
                if n = 2 it returns the index and the lowest value;
                if n = 3 it returns the index and the highest value,
                    and the index and the lowest value respectively. (Type: Integer)
        arr: Enter an array. (Type: List)
        sm: 
    Returns:
        sm == False:
            n == 1: iMax, vMax (Type: Integer)
            n == 2: iMin, vMin (Type: Integer)
            n == 3: iMax, vMax, iMin, vMin (Type: Integer)
        sm == True:
            n == 1: s, iMax, vMax (Type: Integer)
            n == 2: s, iMin, vMin (Type: Integer)
            n == 3: s, iMax, vMax, iMin, vMin (Type: Integer)
    Examples:
        iH, vH = hl(1,arr)
        iL, vL = hl(2, arr)
        iH2, vH2, iL2, vL2 = hl(3, arr)

        or 

        s, iH, vH = hl(1, arr , True)
        s, iL, vL = hl(2, arr, True)
        s, iH2, vH2, iL2, vL2 = hl(3, arr, True)
    '''
    vMax = 0
    vMin = arr[0]
    iMax = 0
    iMin = 0
    s = 0

    for i in arr:
        s += i

    if sm == False:
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

    else:
        if n == 1:
            for i in range(len(arr)):
                if vMax < arr[i]:
                    vMax = arr[i]
                    iMax = i
            return s, iMax, vMax

        elif n == 2:
            for i in range(len(arr)):
                if vMin > arr[i]:
                    vMin  = arr[i]
                    iMin = i
            return s, iMin, vMin

        elif n == 3:
            for i in range(len(arr)):
                if vMax < arr[i]:
                    vMax = arr[i]
                    iMax = i
                if vMin > arr[i]:
                    vMin  = arr[i]
                    iMin = i
            return s, iMax, vMax, iMin, vMin

        else:
            print('Invalid parameters, please read the documentation.')

def main():

    arr = createArray(5)
    arr = fillArray(arr)

    s, _, vH2, _, _ = hls(3, arr, True)
    
    print('\nThe total number is {},\nthe largest number is {},\nand the sum of all numbers is {},\nand the average of the numbers is: {}'.format(len(arr), vH2, s, (s/(len(arr)))))

if __name__ == "__main__":
    main()
