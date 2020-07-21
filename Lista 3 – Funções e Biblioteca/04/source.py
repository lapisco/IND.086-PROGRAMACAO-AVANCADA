# !/usr/bin/python3
# coding: utf-8

# Created by iagsoncarlos on Tuesday, June 16, 2020.
# Copyright (c) 2020 @iagsoncarlos. All rights reserved.

# --------------------------------------------------------------------------

def equation(ax2, bx, c, flag=False):
    '''
    * equation: Calculates the roots of the second degree equation. * 

    Parameters:
        ax2 =  It is any number and are called the coefficients of the equation. (Type: Integer)
        bx = It is any number and are called the coefficients of the equation. (Type: Integer)
        c = It is any number and are called the coefficients of the equation. (Type: Integer)

    Returns:
        n: Returns a vector with the information, always returning:
            info: Results information. (Type: String)
            delta: Delta, which is the Discriminant value. (Type: Integer or Float)
            x1: Real root 1. (Type: Integer or Float)
            x2: Real root 2. (Type: Integer or Float)
        In that order, if you have those variables. (Type: List)

    Example:

        How to read the results:
            res = equation(1, -2, -1)
            output = ['INFO','Delta', 'X1', 'X2']

            for i in range (len(res)):
                print('{}: {}'.format(output[i], res[i]))

        Result:
            INFO: The delta is greater than zero, the equation has two real and distinct values.
            Delta: 8
            X1: 2.414213562373095
            X2: -0.41421356237309515
    '''
    print('\nTyped function: {}x^2 {}x {} = 0\n'.format(ax2, bx, c))

    if flag == True:
        import matplotlib.pyplot as plt
        import numpy as np

    result = []
    
    delta = (bx**2) - (4 * ax2 * c)

    if delta > 0:
        info = 'The delta is greater than zero, the equation has two real and distinct values.'
        x1 = (-bx + delta**(0.5)) / (2.0 * ax2)
        x2 = (-bx - delta**(0.5)) / (2.0 * ax2)
        result = info, delta, x1, x2

        if flag == True:

            axis_x = []
            axis_y = []
            zeros = []
            axis_xn = []
            axis_yn = []

            variacao = abs(x1 - x2)
            if variacao < 3:
                variacao = 3

            for x in np.arange(x1 - variacao, x2 + variacao, variacao / 100):
                y = ax2 * (x ** 2 ) + bx * (x) + c

                axis_x.append(x)
                axis_y.append(y)
                zeros.append(0.0)
                axis_xn.append(-x)
                axis_yn.append(-y)

            plt.title('Graph of the Quadratic Function')
            plt.xlabel('X')
            plt.ylabel('Y')
            plt.plot(axis_x, axis_y, color="red")
            plt.plot(axis_x, zeros, color="black")
            plt.plot(zeros, axis_y, color="black")
            plt.plot(zeros, axis_yn, color="black")
            plt.scatter(x1, 0, marker='x', color='blue')
            plt.scatter(x2, 0, marker='x', color='blue')
            plt.text(x1, 1.5, ('' + str(x1)))
            plt.text(x2, 1.5, ('' + str(x2)))

            plt.show()

        return result

    elif delta == 0:
        info = 'The delta is equal to zero, the equation has only one real value or two equal results.'
        x1 = (-bx + delta**(0.5)) / (2.0 * ax2)
        x2 = x1
        result = info, delta, x1, x2

        if flag == True:
            axis_x = []
            axis_y = []
            zeros = []
            axis_xn = []
            axis_yn = []

            variacao = abs(x1 - x2)
            if variacao < 3:
                variacao = 3

            for x in np.arange(x1 - variacao, x2 + variacao, variacao / 100):
                y = ax2 * (x ** 2 ) + bx * (x) + c
                
                axis_x.append(x)
                axis_y.append(y)
                zeros.append(0.0)
                axis_xn.append(-x)
                axis_yn.append(-y)

            plt.title('Graph of the Quadratic Function')
            plt.xlabel('X')
            plt.ylabel('Y')
            plt.plot(axis_x, axis_y, color="red")
            plt.plot(axis_x, zeros, color="black")
            plt.plot(zeros, axis_y, color="black")
            plt.plot(zeros, axis_yn, color="black")
            plt.scatter(x1, 0, marker='x', color='blue')
            plt.scatter(x2, 0, marker='x', color='blue')
            plt.text(x1, 1.5, ('' + str(x1)))
            plt.text(x2, 1.5, ('' + str(x2)))

            plt.show()

        return result

    else:
        info = 'The delta value is less than zero, the equation has no real values.'
        result = info, delta

        x1 = x2 = 0

        if flag == True:
            axis_x = []
            axis_y = []
            zeros = []
            axis_xn = []
            axis_yn = []

            variacao = abs(x1 - x2)
            if variacao < 3:
                variacao = 3

            for x in np.arange(x1 - variacao, x2 + variacao, variacao / 100):
                y = ax2 * (x ** 2 ) + bx * (x) + c
                
                axis_x.append(x)
                axis_y.append(y)
                zeros.append(0.0)
                axis_xn.append(-x)
                axis_yn.append(-y)

            plt.title('Graph of the Quadratic Function')
            plt.xlabel('X')
            plt.ylabel('Y')
            plt.plot(axis_x, axis_y, color="red")
            plt.plot(axis_x, zeros, color="black")
            plt.plot(zeros, axis_y, color="black")
            plt.plot(zeros, axis_yn, color="black")
            plt.scatter(x1, 0, marker='x', color='blue')
            plt.scatter(x2, 0, marker='x', color='blue')
            plt.text(x1, 1.5, ('' + str(x1)))
            plt.text(x2, 1.5, ('' + str(x2)))

            plt.show()


        return result

def main():
    # INFO: If you want to enter a float value, change the way to switch to the function.
    a = int(input('Enter the Ax^2: '))
    b = int(input('Enter the Bx: '))
    c = int(input('Enter the C: '))

    # res = equation(1, -2, -1)
    res = equation(a, b, c, True)

    output = ['INFO','Delta', 'X1', 'X2']

    for i in range (len(res)):
        print('{}: {}'.format(output[i], res[i]))

if __name__ == "__main__":
    main()