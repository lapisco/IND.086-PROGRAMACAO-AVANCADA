# !/usr/bin/python3
# coding: utf-8

# Created by iagsoncarlos on Tuesday, June 16, 2020.
# Copyright (c) 2020 @iagsoncarlos. All rights reserved.

# --------------------------------------------------------------------------

def divisors(n):
    '''
    * divisors: Calculates all the divisors of a given number. *

    Parameters:
        n: Enter an integer value. (Type: Integer)
    Returns:
        res: Returns an array of all found dividers. (Type: List)
    '''
    res = []
    for i in range(1, n + 1):
        if ((n % i) == 0): 
            res.append(i)

    return res

def main():
    value = int(input('Enter an integer value: '))

    result = divisors(value)
    print('\n{} dividers were found for number {}.\nDividers: {}'.format((len(result)), value, result))

if __name__ == "__main__":
    main()