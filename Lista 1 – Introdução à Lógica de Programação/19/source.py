# !/usr/bin/python3
# coding: utf-8

# Created by iagsoncarlos on Tuesday, June 16, 2020.
# Copyright (c) 2020 @iagsoncarlos. All rights reserved.

# --------------------------------------------------------------------------

def pi():
    '''
    * pi: Series/Sequence *

    Parameters:
        None: (Type: None)
    Returns:
        The function returns the result of the Series/Sequence. (Type: Float)

        return ser
    '''
    sign = 0
    ser = k = 4

    for i in range(3, 31, 2):
        if sign == 0:
            ser -= (k / i)
            sign = 1

        else:
            ser += (k / i)
            sign = 0
    
    print(ser)
    return ser
            

def main():

    result = pi()
    print('\nThe result of the series is: ', result)

if __name__ == "__main__":
    main()