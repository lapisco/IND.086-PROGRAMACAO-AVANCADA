# !/usr/bin/python3
# coding: utf-8

# Created by iagsoncarlos on Tuesday, June 16, 2020.
# Copyright (c) 2020 @iagsoncarlos. All rights reserved.

# --------------------------------------------------------------------------

def combinatorial(arr1, arr2):
    '''
    * combinatorial: Possible combinations between two arrays *
    
    Parameters:
        arr1: It is an array, provided by the user. (Type: List)
        arr2: It is an array, provided by the user. (Type: List)
    Returns:
        comb: The function returns an array with the possible combinations
        between the two input arrays of the function. (Type: List)
    '''
    comb = []

    count = 0
    for i in arr1:
        for j in arr2:
            count += 1
            comb.append([i, j])
            
    return comb

def main():

    dice = [1, 2, 3, 4, 5, 6]

    result = combinatorial(dice, dice)

    print('\nThere are a total of {} possible combinations.\n\nAnd they are:\n'.format(len(result)))
    for i in result:
        print(i)

if __name__ == "__main__":
    main()