# !/usr/bin/python3
# coding: utf-8

# Created by iagsoncarlos on Tuesday, June 16, 2020.
# Copyright (c) 2020 @iagsoncarlos. All rights reserved.

# --------------------------------------------------------------------------

def mati(mass):
    '''
    * mati: Calculate mass and remaining time of the material *

    Parameters:
        mass: It is an integer, provided by the user. The mass value of the material (Type: Float)
    Returns:
        The function returns the initial mass, the final mass and the calculated time in seconds. (Type: Float)
            
            return mass, finalMa, totalTi (Type: Float)
    INFO:
        About return units:
            mass: Unit is grams
            finalMa: Unit is grams
            totalTi: Unit is seconds
    '''
    finalMa = 0.5
    initialMa = mass
    totalTi = 0

    while (initialMa > finalMa):
        initialMa /= 2
        totalTi += 50

    return mass, finalMa, totalTi

def main():
    ma = float(input('Enter the mass value of the material: '))

    initial, final, total = mati(ma)

    print('\nThe initial mass is {}g,\nThe final mass is {}g,\nAnd took a total time of {}s.'. format(initial, final, total))

if __name__ == "__main__":
    main()