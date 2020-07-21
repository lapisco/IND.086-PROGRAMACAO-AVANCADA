# !/usr/bin/python3
# coding: utf-8

# Created by iagsoncarlos on Tuesday, June 16, 2020.
# Copyright (c) 2020 @iagsoncarlos. All rights reserved.

# --------------------------------------------------------------------------

def average(n1, n2, threshold, ui):
    '''
    * average: Average between two notes *

    Parameters:
        n1: It is an integer, provided by the user. (Type: Integer or Float)
        n2: It is an integer, provided by the user. (Type: Integer or Float)
        threshold: It is the average to decide the result, the comparison threshold. (Type: Integer or Float)
        ui: UI – User Interface, if true, the result will be displayed in text mode, in addition to the numeric return. (Type: Boolean)
    Returns:
        n: Returns the average of the two values passed, and returns 1 if it passes or 0 if it fails. (Type: Float, Integer)
    Example:
        average, result = average(2, 8, 5, True)
    '''
    flag = ui
    temp = ((n1 + n2) / 2)
    if temp > threshold:
        if flag == True:
            print('\nApproved!')
        else:
            pass
        return (temp, 1)
    else:
        if flag == False:
            print('\nDisapproved!')
        else:
            pass
        return (temp, 0)
        
# Main function
def main():
    # INFO: If you want to enter a float value, change the way to switch to the function.
    num1 = int(input('Enter the first note: '))
    num2 = int(input('Enter the second note: '))

    av, res = average(num1, num2, 5, False)

    flag = ''
    if res == 1:
        flag = 'Approved!'
    else:
        flag = 'Disapproved!'

    print('\nThe average is: {} ({})'.format(av, flag))

if __name__ == "__main__":
    main()