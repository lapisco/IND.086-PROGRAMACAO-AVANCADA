# !/usr/bin/python3
# coding: utf-8

# Created by iagsoncarlos on Tuesday, June 16, 2020.
# Copyright (c) 2020 @iagsoncarlos. All rights reserved.

# --------------------------------------------------------------------------

def fibonacci(n):
    '''
    * fibonacci: Fibonacci sequence *

    Parameters:
        n: It is an integer, provided by the user. (Type: Integer)
    Returns:
        The function returns the result of the Fibonacci sequence. (Type: List)
        
        return ser
    '''
    ser = []

    previous = nxt = 0
    while(nxt < n):
        ser.append(nxt)
        nxt = nxt + previous
        previous = nxt - previous
        if(nxt == 0):
            nxt = nxt + 1

    return ser

def main():

    number = int(input('Enter an integer value: '))
    # result = fibonacci(4750)
    result = fibonacci(number)

    print('\nFibonacci sequence with {} elements.\nThe elements are: {}'.format((len(result)), result))

if __name__ == "__main__":
    main()