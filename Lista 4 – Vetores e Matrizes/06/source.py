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

def exclusiveFill(arr):
    '''
    * exclusiveFill: Exclusive filling, repetition of numbers not allowed. *

    Parameters:
        arr: Enter an array. (Type: List)
    Returns:
        arr: Returns a new array with the positions filled by the user without repetition. (Type: List)
    '''
    for i in range(len(arr)):
        if i == 0:
            temp = int(input('Enter the value of position {}: '.format(i)))
            arr[i] = temp
        else:
            temp = int(input('Enter the value of position {}: '.format(i)))
            while (temp in arr) == True:
                print('Value already exists in the array! Please, try again!')
                temp = int(input('Enter the value of position {}: '.format(i)))
            arr[i] = temp
    return arr

def main():
    arr = createArray(10)
    aux = exclusiveFill(arr)

    readArray(aux)

if __name__ == "__main__":
    main()