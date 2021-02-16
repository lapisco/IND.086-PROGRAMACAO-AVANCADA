# !/usr/bin/python3
# coding: utf-8

# Created by iagsoncarlos on Tuesday, June 16, 2020.
# Copyright (c) 2020 @iagsoncarlos. All rights reserved.

# --------------------------------------------------------------------------

def sqrtApproximation(n, ap):
    '''
    * sqrtApproximation: Newton's successive approximation method *

    Parameters:
        n: It is an integer, provided by the user. (Type: Integer)
        ap: It is the number of desired approaches. (Type: Integer)
    Returns:
        Returns the result of the square root of the number entered
        by Newton's successive approximation method. (Type: Float)
    '''
    root = n/2
    for i in range(ap):
        root = ((root * root) + n) / (2 * root)

    print('\nThe root of {} is {} with {} approximations used.'.format(n, root, ap))
    return root

def main():
    n = int(input('Enter an integer value: '))
    ap = int(input('What number of approaches is desired? '))

    result = sqrtApproximation(n, ap)

    print('\nThe function returns the value: ', result)

if __name__ == "__main__":
    main()