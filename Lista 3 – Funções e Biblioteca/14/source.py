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

def exponential(n):
    '''
    * exponential: Approximation of the exponential function *

    Parameters:
        n: It is an integer, provided by the user. (Type: Integer)

    Returns:
        The function returns the approximation of the exponential function. (Type: Float)
        
        return exp
    '''
    exp = n
    for i in range(1, 21):
        exp += ((pow(n, i))/factorial(i))

    return exp

def main():

    num = int(input('Enter an integer value: '))
    result = exponential(num)

    print('\nThe result of the approximation of the exponential function is: ', result)

if __name__ == "__main__":
    main()