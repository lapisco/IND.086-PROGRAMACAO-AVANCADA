# !/usr/bin/python3
# coding: utf-8

# Created by iagsoncarlos on Tuesday, June 16, 2020.
# Copyright (c) 2020 @iagsoncarlos. All rights reserved.

# --------------------------------------------------------------------------

def chessboard():
    '''
    * chessboard: Calculates how many corn kernels can be added to the tray. *

    Parameters:
        None: (Type: None)
    Returns:
        The function returns how many corn kernels can be added to the tray,
        taking into account that the next position takes twice the amount of the previous one. (Type: Interger)
    '''
    corn = 1
    for i in range(1, 64):
        corn *= 2

    print(corn)
    return corn
    

def main():
    chessboard()

if __name__ == "__main__":
    main()