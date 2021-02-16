# !/usr/bin/python3
# coding: utf-8

# Created by iagsoncarlos on Tuesday, June 16, 2020.
# Copyright (c) 2020 @iagsoncarlos. All rights reserved.

# --------------------------------------------------------------------------

def management():
    '''
    * management: Records genders and ages *

    Parameters:
        None: None
            The function prompts you to enter a String (M / F),
            and an integer value. If the String is different from (M or F)
            the registration will be finalized. (Type: String and Integer)
    Returns:
        The function returns two vectors of type List, one for Male and one for Female, respectively,
        containing integer values, or 0 cases is empty. (Type: List)

            1st: male = []
            2nd: female = []

            return male, female
    '''
    male = []
    female = []

    count = 0
    while True:
        count += 1
        gender = input('M/F: ')
        if (gender == 'M' or gender ==  'm' or gender == 'F' or gender == 'f'):
            age = int(input('Age: '))
            if gender == 'M' or gender == 'm':
                male.append(age)
            else:
                female.append(age)

        else:
            print('\nRegistration completed!')
            if count == 1:
                print('\nList empty!')
                return male, female
                break
            else:
                return male, female
                break

def average(arr):
    '''
    * average: Average of the array values *

    Parameters:
        arr: Enter an array. (Type: List)
    Returns:
        The function returns the average of the values of each position in the array. (Type: Float)
    '''
    s = 0
    for i in arr:
        s += i

    return (s/(len(arr)))

def main():

    m, f = management()
    
    print('''
    Total members is: {}
    Total male members: {}
    Total female members: {}
    Average age (Male): {}
    Average age (Female): {}
    '''.format((len(m + f)), (len(m)), (len(f)), average(m), average(f)))

if __name__ == "__main__":
    main()