# !/usr/bin/python3
# coding: utf-8

# Created by iagsoncarlos on Tuesday, June 16, 2020.
# Copyright (c) 2020 @iagsoncarlos. All rights reserved.

# --------------------------------------------------------------------------

def double(n):
    '''
    * double: Returns twice the entry number *

    Parameters:
        n: It is an integer, provided by the user. (Type: Integer)
    Returns:
        n: Returns twice the entry number. (Type: Integer)
    '''
    return n * 2

def main():
    value = float(input('Enter a value: '))
    aux = double(value)
    print('\nThe value is {:.2f}'.format(aux))

if __name__ == "__main__":
    main()