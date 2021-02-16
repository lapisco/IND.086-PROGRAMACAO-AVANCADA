# !/usr/bin/python3
# coding: utf-8

# Created by iagsoncarlos on Tuesday, June 16, 2020.
# Copyright (c) 2020 @iagsoncarlos. All rights reserved.

# --------------------------------------------------------------------------

def hld(*args):
    '''
    * hld: Higher and lower number, and the difference between them *

    Parameters:
        *args: Input parameter of the function that receives N values. (Type: List)
    Returns:
        The function returns the largest, smallest and the difference between the values entered. (Type: Integer)
        Return higher, lower, (higher-lower)
    Example:
        high, low, diff = hld(10, 20, 80, 3)

        Result:
            print('Higher: {}\nLower: {}\nDifference between them: {}'.format(high, low, diff))
    '''
    higher = 0
    lower = args[0]
    for i in args:
        if i > higher:
            higher = i
        if i < lower:
            lower = i

    # print('Higher: {}\nLower: {}\nDifference between them: {}'.format(higher, lower, (higher-lower)))
    return higher, lower, (higher-lower)

def main():
    # INFO: If you want to enter a float value, change the way to switch to the function.
    a = float(input('Enter 1st number: '))
    b = float(input('Enter 2nd number: '))
    c = float(input('Enter 3rd number: '))
    d = float(input('Enter 4th number: '))
    
    high, low, diff = hld(a, b, c, d)
    print('\nHigher: {}\nLower: {}\nDifference between them: {}'.format(high, low, diff))
    

if __name__ == "__main__":
    main()