# !/usr/bin/python3
# coding: utf-8

# Created by iagsoncarlos on Tuesday, June 16, 2020.
# Copyright (c) 2020 @iagsoncarlos. All rights reserved.

# --------------------------------------------------------------------------

def factorial(x):
    '''
    * factorial: Factorial *

    Parameters:
        x: It is an integer, provided by the user. (Type: Integer)
    Returns:
        Returns the number factorial if it meets the mathematical properties, otherwise it returns None. (Type: Integer or None)
    '''
    if x < 0:
        # print('There is no factorial for negative numbers.')
        return None

    elif x > 0 and x < 2:
        # print('The factorial of {} is 1'.format(x))
        return 1

    else:
        result = 1
        for i in range(2, x + 1):
            result *= i
        # print('The factorial of {} is {}'.format(x, result))
        return result

def cos(n):
    '''
    * cos: Approximation of the Cosine function *

    Parameters:
        n: It is an float, provided by the user. (Type: Float)

    Returns:
        The function returns the approximation of the Cosine function. (Type: Float)
        
        return cosine
    '''
    cosine = 1
    sign = 0
    for i in range(2, 22, 2):
        if (sign % 2) == 0:
            cosine -= (pow(n, i)/factorial(i))
            sign = 1
        else:
            cosine += (pow(n, i)/factorial(i))
            sign = 0

    return cosine

def main():

    num = float(input('Enter an float value: '))
    result = cos(num)

    print('\nThe result of the approximation of the Cosine function is: ', result)

if __name__ == "__main__":
    main()