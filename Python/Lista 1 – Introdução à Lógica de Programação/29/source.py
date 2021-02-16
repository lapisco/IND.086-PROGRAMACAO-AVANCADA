# !/usr/bin/python3
# coding: utf-8

# Created by iagsoncarlos on Tuesday, June 16, 2020.
# Copyright (c) 2020 @iagsoncarlos. All rights reserved.

# --------------------------------------------------------------------------

def hls(n, arr, sm=False):
    '''
    * hls: Higher, Lower Value and Sum of the numbers. *

    Parameters:
        n: Defines the desired return by the function user.
           There are three possible returns:
                if n = 1 it returns the index and the highest value;
                if n = 2 it returns the index and the lowest value;
                if n = 3 it returns the index and the highest value,
                    and the index and the lowest value respectively. (Type: Integer)
        arr: Enter an array. (Type: List)
        sm: 
    Returns:
        sm == False:
            n == 1: iMax, vMax (Type: Integer)
            n == 2: iMin, vMin (Type: Integer)
            n == 3: iMax, vMax, iMin, vMin (Type: Integer)
        sm == True:
            n == 1: s, iMax, vMax (Type: Integer)
            n == 2: s, iMin, vMin (Type: Integer)
            n == 3: s, iMax, vMax, iMin, vMin (Type: Integer)
    Examples:
        iH, vH = hl(1,arr)
        iL, vL = hl(2, arr)
        iH2, vH2, iL2, vL2 = hl(3, arr)

        or 

        s, iH, vH = hl(1, arr , True)
        s, iL, vL = hl(2, arr, True)
        s, iH2, vH2, iL2, vL2 = hl(3, arr, True)
    '''
    vMax = 0
    vMin = arr[0]
    iMax = 0
    iMin = 0
    s = 0

    for i in arr:
        s += i

    if sm == False:
        if n == 1:
            for i in range(len(arr)):
                if vMax < arr[i]:
                    vMax = arr[i]
                    iMax = i
            return iMax, vMax

        elif n == 2:
            for i in range(len(arr)):
                if vMin > arr[i]:
                    vMin  = arr[i]
                    iMin = i
            return iMin, vMin

        elif n == 3:
            for i in range(len(arr)):
                if vMax < arr[i]:
                    vMax = arr[i]
                    iMax = i
                if vMin > arr[i]:
                    vMin  = arr[i]
                    iMin = i
            return iMax, vMax, iMin, vMin

        else:
            print('Invalid parameters, please read the documentation.')

    else:
        if n == 1:
            for i in range(len(arr)):
                if vMax < arr[i]:
                    vMax = arr[i]
                    iMax = i
            return s, iMax, vMax

        elif n == 2:
            for i in range(len(arr)):
                if vMin > arr[i]:
                    vMin  = arr[i]
                    iMin = i
            return s, iMin, vMin

        elif n == 3:
            for i in range(len(arr)):
                if vMax < arr[i]:
                    vMax = arr[i]
                    iMax = i
                if vMin > arr[i]:
                    vMin  = arr[i]
                    iMin = i
            return s, iMax, vMax, iMin, vMin

        else:
            print('Invalid parameters, please read the documentation.')

def storage2():
    '''
    * storage2: Store positive and negative results added by the user. *

    Parameters:
        None: None
            The function prompts you to enter a floating value, the value will be stored in an array [stg],
            And store the weights in the vector [stg] until you find the flag
            which is the stop condition, the entry of the value 1000. (Type: Float)
    Returns:
        The function returns an integer value with the added numbers and a vector with all the numbers,
        or returns 0 and an empty vector, if the first number is 1000, given the stop condition. (Type: Integer and List)

        return counter, stg
    '''
    stg = []
    counter = 0

    print('\nValue you want to store:')

    while True:
        counter += 1
        val = float(input('Value [{}]: '.format(counter)))

        if val == 1000:
            print('\nStorage finished!')
            if counter == 1:
                counter = 0
                print('\nEmpty vector!')
                return counter, stg
            break
        else:
            stg.append(val)

    return counter, stg

def main():

    _, temp = storage2()
    s, _, vH2, _, vL2 = hls(3, temp, True)
    
    print('\nThe total number is {},\nthe biggest number is {},\nthe lowest note is {},\nand the sum of all numbers is {},\nand the average of the numbers is {}'.format(len(temp), vH2, vL2, s, (s/(len(temp)))))

if __name__ == "__main__":
    main()