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
        # print('\nThe time entered was: ' + str(h) + ':' + str(m) + ':' + str(s))
        res = (h * 3600) + (m * 60) + s

        return res
    else:
        print('\nThe values entered do not meet the parameters, please read the documentation.\nInvalid format, try 23:59:59')
        return None

def time():
    '''
    * time: Time difference *

    Parameters:
        The function prompts you to enter numbers of the whole type, in the 24h time format. (Type: Integer)
            Time format: HH:MM:SS == 23:59:59
    Returns:
        The function returns the time difference in input format, 24h,
        with hours in position 0 of the vector, minutes in position 1 and seconds in position 2.
        If the input format is invalid, the application will be interrupted
        and a message will be returned to the user informing you about the error. (Type: List)

        return total
    '''
    # Import from required libraries
    import sys

    time1 = []
    time2 = []
    total = []*3

    title = ['hours', 'minutes', 'seconds']
    for i, j in enumerate(title):
        temp = int(input('Enter an {} value: '.format(j)))
        if i == 0:
            if temp <= 23:
                time1.append(temp)
            else:
                print('Invalid format!')
                sys.exit()
        else:
            if temp <= 59:
                time1.append(temp)
            else:
                print('Invalid format!')
                sys.exit()

    for i, j in enumerate(title):
        temp = int(input('Enter an {} value: '.format(j)))
        if i == 0:
            if temp <= 23:
                time2.append(temp)
            else:
                print('Invalid format!')
                sys.exit()
                
        else:
            if temp <= 59:
                time2.append(temp)
            else:
                print('Invalid format!')
                sys.exit()

    print('\nTime 1: {}\nTime 2: {}'.format(time1, time2))

    time1seg = hms2s(time1[0], time1[1], time1[2])
    time2seg = hms2s(time2[0], time2[1], time2[2])

    if time1seg > time2seg:
        diff = time1seg - time2seg
    else:
        diff = time2seg - time1seg

    if diff >= 3600:
        div = int(diff/3600)
        total.append(div)
        if (diff % 3600) != 0:
            rest = diff % 3600
            if rest >= 60:
                div = int(rest/60)
                total.append(div)
                if (rest % 60) != 0:
                    aux = rest % 60
                    total.append(aux)
                else:
                    total.append(0)
            else:
                total.append(0)
                total.append(rest)
        else:
            total.append(0)
            total.append(0)
            
    elif diff < 3600:
        total.append(0)
        if diff >= 60:
            div = int(diff/60)
            total.append(div)
            if (diff % 60) != 0:
                aux = diff % 60
                total.append(aux)
            else:
                total.append(0)
        else:   
            total.append(0)
            total.append(diff)

    return total

def main():
    result = time()
    print(result)

    print('\nThe difference between time 1 and time 2 is: \n')
    title = ['Hours: ', 'Minutes: ', 'Seconds: ']
    for i, j in enumerate(title):
        print(j + str(result[i]))

    print('\nTotal time difference: {}'.format(result))

if __name__ == "__main__":
    main()