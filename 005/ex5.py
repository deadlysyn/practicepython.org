#!/usr/bin/env python
#
# practicepython.org exercise 5:
# given two lists, print common elements but don't repeat.


import random


def gen_lists(max_size=100, max_num=1000):
    """generate two random lists and return as tuple"""
    _a = []
    _a_size = random.randrange(0, max_size)

    _b = []
    _b_size = random.randrange(0, max_size)

    _x = 0
    while _x < _a_size:
        _a.append(random.randint(0, max_num))
        _x += 1

    _x = 0
    while _x < _b_size:
        _b.append(random.randint(0, max_num))
        _x += 1

    return((_a, _b))


#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
a, b = gen_lists()
result = []

# as a loop...
for x in a:
    if x in b:
        result.append(x)

if set(result):
    print(set(result))
else:
    print('No common elements.')

# listcomp...can return empty set.
print(set([x for x in a if x in b]))
