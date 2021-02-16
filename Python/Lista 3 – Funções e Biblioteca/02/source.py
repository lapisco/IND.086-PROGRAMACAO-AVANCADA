# !/usr/bin/python3
# coding: utf-8

# Created by iagsoncarlos on Tuesday, June 16, 2020.
# Copyright (c) 2020 @iagsoncarlos. All rights reserved.

# --------------------------------------------------------------------------

def simpleCalc(op, n1, n2):
    '''
    * simpleCalc: Simple calculator between two numbers *

    Parameters:
        op: It is the input parameter that determines which operation to perform between the two input numbers. (Type: Integer)
            op = 1: Addition
            op = 2: Subtraction
            op = 3: Multiplication
            op = 4: Division
        n1: It is an integer, provided by the user. (Type: Integer)
        n2: It is an integer, provided by the user. (Type: Integer)
    Returns:
        n: Returns the result of the operation or a message stating the error. (Type: Integer or Float)
    '''
    if op == 1:
        return n1 + n2

    elif op == 2:
        return n1 - n2

    elif op == 3:
        return n1 * n2

    elif op == 4:
        return n1 / n2

    else:
        print('Invalid parameters, please read the documentation.')

def main():
    num1 = int(input('Enter the first value: '))
    num2 = int(input('Enter the second value: '))

    #INFO: Read the documentation to understand the function parameters.
    print('''
    ------- MENU --------

    Addition .......... 1
    Subtraction ....... 2
    Multiplication .... 3
    Division .......... 4
    ''')
    option = int(input('Here: '))
    print('\nThe result of the operation is: {}'.format(simpleCalc(option, num1, num2)))

if __name__ == "__main__":
    main()