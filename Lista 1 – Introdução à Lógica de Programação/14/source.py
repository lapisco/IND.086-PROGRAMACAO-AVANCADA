# !/usr/bin/python3
# coding: utf-8

# Created by iagsoncarlos on Tuesday, June 16, 2020.
# Copyright (c) 2020 @iagsoncarlos. All rights reserved.

# --------------------------------------------------------------------------

def populationRate(ca, gra, cb, grb, flag=False):
    '''
    * populationRate: Calculation of the population rate of city A in relation to city B. *
    
    Parameters:
        ca: The Population of city A. (Type: Float)
        gra: The population growth rate of city A. (Type: Float)
        cb: The Population of city B. (Type: Float)
        grb: The population growth rate of city B. (Type: Float)
        flag: If the flag is true, in addition to the calculated values, the graph of the population growth of cities
        is displayed. (Type: Boolean)
    Returns:
        The function returns how many years it will take for city A to have a larger population than city B.
        And the total population values for city A and B (respectively). (Type: Integer and Float)

            years: (Type: Integer)
            ca: (Type: Float)
            cb: (Type: Float)
    
            return years, ca, cb
    Example:
        result, b, a = populationRate(12000, 0.15, 52000, 0.10, True)
    '''
    years = 0
    ca_list = []
    cb_list = []
    years_list = []

    while(ca < cb):

        ca += (ca * gra)
        cb += (cb * grb)

        years += 1

        if flag == True:
            ca_list.append(ca)
            cb_list.append(cb)
            years_list.append(years)

    print('\nAfter {} years the population of city A ({:.2f}) is larger than city B ({:.2f}).'.format(years, cb, ca))

    if flag == True:
        import matplotlib.pyplot as plt
        import numpy as np

        x1 =  np.arange(len(ca_list))
        x2 = [x + 0.25 for x in x1]

        plt.bar(x1, ca_list, width=0.25, label = 'City A Total: ' + str(ca), color = 'purple')
        plt.bar(x2, cb_list, width=0.25, label = 'City B Total: ' + str(cb), color = 'pink')

        plt.xticks([x + 0.25 for x in range(len(ca_list))], years_list)

        plt.legend()
        plt.title("Population Rate")
        plt.xlabel('Years')
        plt.ylabel('Population')
        plt.show()

    return years, ca, cb

def main():
    ca = float(input('Enter the population of city A: '))
    gra = float(input('Enter the population growth rate of city A: '))
    cb = float(input('Enter the population of city B: '))
    grb = float(input('Enter the population growth rate of city B: '))

    result, b, a = populationRate(ca, gra, cb, grb, True)

if __name__ == "__main__":
    main()