#!/usr/bin/env python
#
# practicepython.org exercise 15:
# reverse word order in strings


def reverse_string(string):
    """pass in a string, get the reverse!"""
    # the magic one-liner!
    return ' '.join(string.split()[::-1])
# ugly attempt #1
#    new = string.split()[::-1]
#    for x in new:
#        print(x, end=' ')
#    print('\n')


s = input('Enter a string: ')
print(reverse_string(s))
