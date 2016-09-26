#!/usr/bin/env python
#
# practicepython.org exercise 3:
# given a list, print elements that are less than 5.


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


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# main exercise
for x in a:
    if x < 5:
        print(x)

# extra 1
b = []
for x in a:
    if x < 5:
        b.append(x)
print(b)

# extra 2
print([x for x in a if x < 5])

# extra 3
num = get_num('Enter a number: ')
print([x for x in a if x < num])
