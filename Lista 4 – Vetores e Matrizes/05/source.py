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

def search(n, arr):
    '''
    * search: Search for a value in a given vector *

    Parameters:
        n: Number you want to search for. (Type: Integer)
        arr: Enter an array. (Type: List) 
    Returns:
        Returns an array with the positions/indexes found,-
        -or the information that the number does not exist in the array.

        return indexes (Type: List)
        return 0 (Type: Integer)
    '''
    indexes = []

    for i in range(len(arr)):
        if n == arr[i]:
            indexes.append(i)
        else:
            pass

    if (len(indexes) != 0):
        print('Have been found {} times'.format(len(indexes)))
        for i in range(len(indexes)):
            print('Value found in position {}'.format(indexes[i]))
        return indexes
    else:
        print('\nValue not found!')
        return 0

def main():
    arr = createArray(8)
    arr = fillArray(arr)
    readArray(arr)

    number = int(input('\nGet the value: '))

    search(number, arr)

if __name__ == "__main__":
    main()