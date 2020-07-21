# !/usr/bin/python3
# coding: utf-8

# Created by iagsoncarlos on Tuesday, June 16, 2020.
# Copyright (c) 2020 @iagsoncarlos. All rights reserved.

# --------------------------------------------------------------------------

def prime(n):
    '''
    * prime: Returns prime numbers *

    Parameters:
        n: It is an integer, provided by the user. (Type: Integer)
    Returns:
        The function returns 1 if the number consulted is prime or returns 0 otherwise. (Type: Integer)
    '''
    k = 0 # Number of dividers
    for i in range(1, n):
        if n % i == 0:
            k = k + 1
            if k > 1:
                break
    if k > 1:
        print('The number entered ({}) is not a Prime number'.format(n))
        return 0

    else:
        print('The number entered ({}) is a Prime number'.format(n))
        return 1

def main():
    n = int(input('Enter an integer value: '))

    result = prime(n)

    print('\nThe function returns the value: ', result)

if __name__ == "__main__":
    main()