# !/usr/bin/python3
# coding: utf-8

# Created by iagsoncarlos on Tuesday, June 16, 2020.
# Copyright (c) 2020 @iagsoncarlos. All rights reserved.

# --------------------------------------------------------------------------

def a():
    '''
    * a: Series/Sequence *

    Parameters:
        None: (Type: None)
    Returns:
        The function returns the result of the Series/Sequence. (Type: Interger)
        
        return ser
    '''
    ser = num = 1

    for i in range(1, 50):
        num += (i * 2) / i
        ser += num/(i+1)

        print(ser)
    return ser

    

def main():

    result = a()
    print('\nThe result of the series is: ', result)

if __name__ == "__main__":
    main()