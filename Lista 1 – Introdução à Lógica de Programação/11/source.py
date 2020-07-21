# !/usr/bin/python3
# coding: utf-8

# Created by iagsoncarlos on Tuesday, June 16, 2020.
# Copyright (c) 2020 @iagsoncarlos. All rights reserved.

# --------------------------------------------------------------------------

def range4square(x, y):
    '''
    * range4square: Returns the square of the numbers between the given range. *

    Parameters:
        x: It is an integer, provided by the user. Start of the range. (Type: Integer)
        y: It is an integer, provided by the user. End of range. (Type: Integer)
    Returns:
        Returns the total number of numbers in the range
        and the square of the numbers between the specified range.

            return ((len(square)), square) (Type: Integer and List)
    '''
    square = []

    for i in range(x, y + 1):
        square.append(i**2)

    return ((len(square)), square)

def main():

    start = int(input('Enter the beginning of the range: '))
    end = int(input('Enter the end of the range: '))

    total, square = range4square(start, end)

    print('\nTotal numbers in the range is {}\nand the square of the numbers between the specified range is: {}'.format(total, square))


# Main function
if __name__ == "__main__":
    main()
