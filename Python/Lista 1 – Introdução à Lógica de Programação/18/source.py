# !/usr/bin/python3
# coding: utf-8

# Created by iagsoncarlos on Tuesday, June 16, 2020.
# Copyright (c) 2020 @iagsoncarlos. All rights reserved.

# --------------------------------------------------------------------------

def m():
    '''
    * m: Series/Sequence *

    Parameters:
        None: (Type: None)
    Returns:
        The function returns the result of the Series/Sequence. (Type: Interger)

        return ser
    '''
    ser = 0
    k = 1

    for i in range(37, 0, -1):
        ser += (i * (i+1)) / k
        k += 1
        
    print(ser)
    return ser
            

def main():

    result = m()
    print('\nThe result of the series is: ', result)

if __name__ == "__main__":
    main()