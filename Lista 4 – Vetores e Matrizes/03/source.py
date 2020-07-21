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

def parity(n, arr):
    '''
    * parity: Returns even and odd numbers in the array. *

    Parameters:
        n: Defines the desired return by the function user.
           There are three possible returns:
                if n = 1 it returns the indexes and the Even values;
                if n = 2 it returns the indexes and the Odd values;
                if n = 3 it returns the indexes and the Even values,
                    and the indexes and the Odd values respectively. (Type: List)
        arr: Enter an array. (Type: List)
    Returns:
        n == 1: iEven, vEven (Type: List)
        n == 2: iOdd, vOdd (Type: List)
        n == 3: iEven, vEven, iOdd, vOdd (Type: List)
    Examples:
        iE, vE = parity(1, arr)
        iO, vO = parity(2, arr)
        iE2, vE2, iO2, vO2 = parity(3, arr)
    '''
    vOdd = []
    iOdd = []
    vEven = []
    iEven = []

    if n == 1:
        for i in range(len(arr)):
            if arr[i]%2 == 0:
                vEven.append(arr[i])
                iEven.append(i)  
            else:
                pass
        return iEven, vEven

    elif n == 2:
        for i in range(len(arr)):
            if arr[i]%2 == 0:
                pass
            else:
                vOdd.append(arr[i])
                iOdd.append(i)
        return iOdd, vOdd

    elif n == 3:
        for i in range(len(arr)):
            if arr[i]%2 == 0:
                vEven.append(arr[i])
                iEven.append(i)  
            else:
                vOdd.append(arr[i])
                iOdd.append(i)
        return iEven, vEven, iOdd, vOdd

    else:
        print('Invalid parameters, please read the documentation.')

def main():
    arr = createArray(10)
    arr = fillArray(arr)
    readArray(arr)

    # iE, vE = parity(1, arr)
    # print('\nEven numbers: ')
    # print('Indexes: {}, Values: {} (respectively)'.format(iE, vE))

    iO, vO = parity(2, arr)
    print('\nOdd numbers: ')
    print('Indexes: {}, Values: {} (respectively)'.format(iO, vO))

    # iE2, vE2, iO2, vO2 = parity(3, arr)
    # print('\nEven and Odd numbers: ')
    # print('Indexes: {}, Values: {} (respectively)'.format(iE2, vE2))
    # print('Indexes: {}, Values: {} (respectively)'.format(iO2, vO2))

if __name__ == "__main__":
    main()