# !/usr/bin/python3
# coding: utf-8

# Created by iagsoncarlos on Tuesday, June 16, 2020.
# Copyright (c) 2020 @iagsoncarlos. All rights reserved.

# --------------------------------------------------------------------------

def digits(n):
    '''
    * digits: The sum of the digits of the number "n". *

    Parameters:
        n: It is an integer, provided by the user. (Type: Integer)
    Returns:
        The function returns the sum between each digit of the number entered by the user. (Type: Integer)
    '''
    add = 0
    for i in list(str(n)):
        add += int(i)

    print('\nThe sum of the digits in the number {} is {}.'.format(n, add))
    return add

def main():
    n = int(input('Enter an integer value: '))

    result = digits(n)

    print('\nThe function returns the value: ', result)

# Main function
if __name__ == "__main__":
    main()