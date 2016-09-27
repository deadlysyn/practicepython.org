#!/usr/bin/env python
#
# practicepython.org exercise 11:
# ask for number and determine if prime


def get_num(prompt='Number? '):
    """prompt for a number"""
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


def is_prime(num):
    """given a number, return True if prime else False"""
    for x in range(2, num + 1):
        if num % x == 0:
            return False
    return True


num = get_num()

if is_prime(num):
    print('Primo!')
else:
    print('Booooooooring.')
