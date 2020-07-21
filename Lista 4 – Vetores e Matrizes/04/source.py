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

def prime(arr):
    '''
    * prime: Returns prime numbers *

    Parameters:
        arr: Number of positions in the array. (Type: List)
    Returns:
        arr: Returns an array with indexes and the prime numbers respectively. (Type: List)
    '''
    import math

    vPrime = []
    iPrime = []

    for i in range(len(arr)):
        for j in range(2, int(math.sqrt(arr[i])) + 1):
            if arr[i] % j != 0:
                vPrime.append(arr[i])
                iPrime.append(i)

    return iPrime, vPrime

def main():
    arr = createArray(10)
    arr = fillArray(arr)
    readArray(arr)

    iPri, vPri = prime(arr)

    print('\nPrime numbers: ')
    print('Indexes: {}, Values: {} (respectively)'.format(iPri, vPri))

if __name__ == "__main__":
    main()