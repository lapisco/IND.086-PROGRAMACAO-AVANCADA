# !/usr/bin/python3
# coding: utf-8

# Created by iagsoncarlos on Tuesday, June 16, 2020.
# Copyright (c) 2020 @iagsoncarlos. All rights reserved.

# --------------------------------------------------------------------------

def triangle(a, b, c):
    '''
    * triangle: Check if it is a triangle, and classify it. *

    Parameters:
        a = It is an integer that represents one side of the triangle. (Type: Integer)
        b = It is an integer that represents one side of the triangle. (Type: Integer)
        c = It is an integer that represents one side of the triangle. (Type: Integer)

    Returns:
        Returns an integer, which classifies the triangle as to its sides,
        or returns None if there are any parameters incompatible with the function. (Type: Integer or None)
    '''
    if a<=0 or b<=0 or c<=0:
        print('\nNull or negative sides are not accepted.\n')
        print('Invalid parameters, please read the documentation.')
        return None
    
    else:
        if a>=b+c or b>=c+a or c>=a+b:
            print('\nNonexistent triangle.')
            return 0

        elif a==b and b==c:
            print('\nEquilateral triangle.')
            return 3

        elif a==b or b==c or c==a:
            print('\nIsosceles triangle.')
            return 1

        else:
            print('\nScalene triangle.')
            return 2

def main():
    # INFO: If you want to enter a float value, change the way to switch to the function.
    a = int(input('Enter side A: '))
    b = int(input('Enter Side B: '))
    c = int(input('Enter Side C: '))

    verf = triangle(a, b, c)

    print('Return: ', verf)

if __name__ == "__main__":
    main()