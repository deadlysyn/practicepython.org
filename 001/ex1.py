#!/usr/bin/env python
#
# practicepython.org exercise 1:
# get name and age, then tell user when they will be 100

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


name = input('\nWhat is your name? ')
age = get_num('\nWhat is your age? ')

cur_year = int(date.today().year)
fut_year = cur_year - age + 100

repeat = get_num('\nHow many messages do you want? ')

if repeat > 20:
    answer = input('\nAre you sure you want such a big number? (y/N) ')
    if answer.lower() != 'y':
        print('OK, resetting to 1...')
        repeat = 1

print('\nHello, {0}... you will be 100 in the year {1}!'
    .format(name.title(), fut_year) * repeat)
