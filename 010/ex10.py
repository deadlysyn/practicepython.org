#!/usr/bin/env python
#
# practicepython.org exercise 10:
# redo exercise 5 a bit differently

import random


# generate two random lists
a = random.sample(range(100), random.randint(1, 100))
b = random.sample(range(100), random.randint(1, 100))

c = set([x for x in a if x in b])

print('a: ', a, '\n')
print('b: ', b, '\n')
print('c: ', c)
