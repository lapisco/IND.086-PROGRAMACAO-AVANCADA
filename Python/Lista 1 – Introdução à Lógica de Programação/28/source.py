# !/usr/bin/python3
# coding: utf-8

# Created by iagsoncarlos on Tuesday, June 16, 2020.
# Copyright (c) 2020 @iagsoncarlos. All rights reserved.

# --------------------------------------------------------------------------

def coordinates(x, y, flag=False):
    '''
    * coordinates: Coordinate with points X and Y. *

    Parameters:
        x: It is an integer, provided by the user. (Type: Integer)
        y: It is an integer, provided by the user. (Type: Integer)
        flag: It is a boolean provided by the user, if True is a function that graphically shows the result,
            otherwise it has no action. (Type: Boolean)
    Returns:
        Returns 1 if the coordinate is within the region of the lines or returns 0 otherwise.
            You can also return the result graphically if the Boolean flag is true. (Type: Integer)
    '''
    origX = x
    origY = y

    if (y <= (3 * x)) and (y >= (x / 3)):
        points = 1
        print('\nThe coordinate entered is inside the region.')
    else:
        points = 0
        print('\nThe coordinate entered is outside the region.')

    if flag == True:
        import numpy as np
        import matplotlib.pyplot as plt

        x = np.arange(-2 * (x+y), 2 * (x+y))
        
        plt.figure(figsize=(6, 4))
        plt.title('Coordinate ({}, {})'.format(origX, origY))
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.plot(x, 3 * x, color='black')
        plt.plot(x, x / 3, color='black')
        plt.fill_between(x, 3 * x, x / 3, facecolor='#dcdcdc', interpolate=True)
        plt.scatter(origX, origY, color='red')
        plt.show()

    return points

def main():
    x = int(input('Enter an integer value for X: '))
    y = int(input('Enter an integer value for Y: '))

    result = coordinates(x, y, True)

    print('\nThe function returns the value: ', result)

if __name__ == "__main__":
    main()