# !/usr/bin/python3
# coding: utf-8

# Created by iagsoncarlos on Tuesday, June 16, 2020.
# Copyright (c) 2020 @iagsoncarlos. All rights reserved.

# --------------------------------------------------------------------------

def ifce(n1, n2, af):
    '''
    * ifce: Evaluation system of the Federal Institute of Ceará (IFCE). *

    Parameters:
        n1: It is the student's first average. (Type: Float)
        n2: It is the student's second average. (Type: Float)
        af: It is of the Boolean type, for the true case the program calculates and returns the minimum for approval in the final exam. (Type: Boolean)
    Returns:
        The function returns a value of type Float or type None.
        If the Boolean flag is True (af), that is, if the student needs af, the function will return none,
        and show the average, and how much it needs in the final exam.
        If the flag is False, the function will return a value of type Float, being 1 if approved or 0 otherwise. (Type: Float or None) 

    SOURCE: https://ifce.edu.br/espaco-estudante/regulamento-de-ordem-didatica/2016-07-08-rod-revisao-aprovada-consup-13jun2016-v30.pdf
    '''
    average = (((2 *n1) + (3 * n2)) / 5)
    
    if average < 3:
        print('\nYou failed the period!\nYour average was {}'.format(average))
        return 0
    elif average > 3 and average < 7:
        if af == True:
            print('\nYour average was {} so you need to score {} in the final exam.'.format(average, (10 - average)))
            return None
        else:
            print('\nYou failed the period!\nYour average was {}'.format(average))
            return 0
    else:
        print('\nYou passed the period!\nYour average was {}'.format(average))
        return 1

def main():
    # INFO: If you want to enter a float value, change the way to switch to the function.
    a = float(input('Enter 1st note: '))
    b = float(input('Enter 2nd note: '))

    av = ifce(a, b, True)

    print('\nReturn: ', av)

if __name__ == "__main__":
    main()