#!/usr/bin/env python
#
# practicepython.org exercise 13:
# print desired number of fibonnaci numbers.


def get_num(prompt='Number? '):
    """helper function to prompt for a number"""
    _num = 0
    while True:
        try:
            _num = int(input(prompt))
        except ValueError:
            print('Was that a number? Try again!')
            continue
        else:
            break
    return _num


def fibs(_count):
    """return desired number of fibs"""
    _fibs = [0, 1]
    if _count == 1:
        return [0]
    elif _count > 1:
        for i in range(_count - 2):
            _fibs.append(_fibs[-2] + _fibs[-1])
        return _fibs
    else:
        return []


l = fibs(get_num())
print(l)
