#!/usr/bin/env python
#
# practicepython.org exercise 14:
# write a function which removes all dupes from a list


def rm_dupes_loop(dupes):
    """pass in a list, get back a list with no dupes"""
    no_dupes = []
    for x in dupes:
        if x in no_dupes:
            pass
        else:
            no_dupes.append(x)
    return no_dupes


def rm_dupes_set(dupes):
    """same as rm_dupes_loop but without a loop!"""
    return list(set(dupes))


a = [1, 1, 2, 3, 4, 5, 5, 5, 6, 7]
b = rm_dupes_loop(a)
c = rm_dupes_set(a)

print(a, '\n', b, '\n', c)
