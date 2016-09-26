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


num = get_num('Enter a number: ')

# with a loop...
result = []
for x in range(1, num + 1):
    if num % x == 0:
        result.append(x)

print(result)

# with a listcomp...
a = list(range(1, num + 1))
b = [x for x in a if num % x == 0]
print(b)
