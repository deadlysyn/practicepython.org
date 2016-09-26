#!/usr/bin/env python
#
# practicepython.org exercise 2:
# ask for number, and respond differently based on even/odd

import sys
from datetime import date


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

number = get_num('Enter a number: ')

if number % 2 == 0:
    if number % 4 == 0:
        print('{0} is divisible by 4!'.format(number))
    else:
        print('{0} is an even number!'.format(number))
else:
    print('{0} is an odd number!'.format(number))

num = get_num('Enter a numerator: ')
check = get_num('Enter a denominator: ')

if num % check == 0:
    print('{0} is divisible by {1}!'.format(num, check))
else:
    print('{0} is not divisible by {1}!'.format(num, check))
