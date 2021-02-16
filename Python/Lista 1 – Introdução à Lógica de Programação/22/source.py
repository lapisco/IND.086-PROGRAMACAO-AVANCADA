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

def alternatingSequence(x):
    '''
    * alternatingSequence: Alternating Sequence *

    Parameters:
        n: None

    Returns:
        The function returns the result of the monotonous sequence. (Type: Float)

            return sers
    '''
    sign = 0
    sers = x
    for i in range(3, 14, 2):

        if (sign % 2) == 0:
            sers -= (pow(x, i)/factorial(i))
            sign = 1
        else:
            sers += (pow(x, i)/factorial(i))
            sign = 0
                
    return sers

def main():

    num = int(input('Enter an integer value: '))
    result = alternatingSequence(num)

    print('\nThe result of the Alternating Sequence is: ', result)

if __name__ == "__main__":
    main()