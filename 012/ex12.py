#!/usr/bin/env python
#
# practicepython.org exercise 10:
# redo exercise 5 a bit differently


def fl_list(list):
    _length = len(list)
    if _length > 0:
        _first = list[0]
        _last = list[_length - 1]
        return [_first, _last]
    else:
        return []


a = [5, 10, 15, 20, 25]
b = fl_list(a)

print(b)
