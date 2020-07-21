# !/usr/bin/python3
# coding: utf-8

# Created by iagsoncarlos on Tuesday, June 16, 2020.
# Copyright (c) 2020 @iagsoncarlos. All rights reserved.

# --------------------------------------------------------------------------

def hms2s(h, m, s):
    '''
    * hms2s: Convert hours:minutes:seconds to seconds. *

    Parameters:
        h: It is an integer, provided by the user. (Type: Integer)
            Accepted range is 0 to 23.
        m: It is an integer, provided by the user. (Type: Integer)
            Accepted range is 0 to 59.
        s: It is an integer, provided by the user. (Type: Integer)
            Accepted range is 0 to 59.
    Returns:
        Returns the total number of seconds of the given time,
        or returns None and a message informing that the values do not meet the parameters. (Type: Integer)
    '''
    if h <= 23 and m <= 59 and s <= 59:
        print('\nThe time entered was: ' + str(h) + ':' + str(m) + ':' + str(s))
        res = (h * 3600) + (m * 60) + s

        return res
    else:
        print('\nThe values entered do not meet the parameters, please read the documentation.\nInvalid format, try 23:59:59')
        return None

def main():
    h = int(input('Enter an integer value: '))
    m = int(input('Enter an integer value: '))
    s = int(input('Enter an integer value: '))

    result = hms2s(h, m, s)

    print('\nThe function returns the value: ', result)

if __name__ == "__main__":
    main()