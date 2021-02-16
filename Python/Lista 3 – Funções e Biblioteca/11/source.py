# !/usr/bin/python3
# coding: utf-8

# Created by iagsoncarlos on Tuesday, June 16, 2020.
# Copyright (c) 2020 @iagsoncarlos. All rights reserved.

# --------------------------------------------------------------------------

def alternatingHarmonic(n):
    '''
    * AlternatingHarmonic: Alternate Harmonica Series *

    Parameters:
        n: Enter an integer. (Type: Integer)

    Returns:
        The function returns the result of the alternating harmonic series. (Type: Float)

            return sers
    '''
    sers = j = 0

    for i in range(25, 0, -1):

        j += 1
        if (i % 2) == 1:
            sers += (pow(n, i)/ j)
        else:
            sers -= (pow(n, i)/ j)

    return sers

def main():

    num = int(input('Enter an integer value: '))

    result = alternatingHarmonic(num)
    print('\nThe result of the series is: ', result)

if __name__ == "__main__":
    main()