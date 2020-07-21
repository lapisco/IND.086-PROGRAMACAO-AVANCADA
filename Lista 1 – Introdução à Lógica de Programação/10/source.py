# !/usr/bin/python3
# coding: utf-8

# Created by iagsoncarlos on Tuesday, June 16, 2020.
# Copyright (c) 2020 @iagsoncarlos. All rights reserved.

# --------------------------------------------------------------------------

def range4class(x, y, flag=2):
    '''
    * range4class: Sort even or odd numbers within the given range. *

    Parameters:
        x: It is an integer, provided by the user. Start of the range. (Type: Integer)
        y: It is an integer, provided by the user. End of range. (Type: Integer)
        flag: It is an integer, provided by the user. (Type: Integer)
            flag = 0: Sorts even numbers in the range. (Type: Integer)
            flag = 1: Sorts odd numbers in the range. (Type: Integer)
            flag = 2: Sorts even and odd numbers in the range. (Type: Integer)
    Returns:
        The function returns the total number of classified numbers,
        as well as the numbers that have been classified.
            flag = 0: return total even numbers, even numbers. (Type: Integer and List)
            flag = 1: return total odd numbers, odd numbers. (Type: Integer and List)
            flag = 2: return total even numbers, even numbers,
                             total odd numbers, odd numbers. (Type: Integer, List and Integer and List)
    '''
    even = []
    odd = []

    if flag == 0:
        for i in range(x, y + 1):
            if (i % 2) == 0:
                even.append(i)
            else:
                pass
        return ((len(even)), even)

    elif flag == 1:
        for i in range(x, y + 1):
            if (i % 2) == 0:
                pass
            else:
                odd.append(i)
        return ((len(odd)), odd)

    elif flag == 2:
        for i in range(x, y + 1):
            if (i % 2) == 0:
                even.append(i)
            else:
                odd.append(i)
        return ((len(even)), even, (len(odd)), odd)

    else:
        print('\nInvalid parameters, please read the documentation.')

def main():

    start = int(input('Enter the beginning of the range: '))
    end = int(input('Enter the end of the range: '))
    # flag = int(input(''))

    _, _, lenOdd, odd = range4class(start, end)

    print('\nThe numbers in the range ({}, {})\nThere are a total of {} odd numbers.\nThe numbers are: {}'.format(start, end, lenOdd, odd))


# Main function
if __name__ == "__main__":
    main()
