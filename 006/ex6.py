#!/usr/bin/env python
#
# practicepython.org exercise 6:
# Ask for string and determine if it is a palindrome.

test_str = input('Enter string to test: ')

rev_str = test_str[::-1]

if test_str.lower() == rev_str.lower():
    print('Congrats, it looks like a palindrome!')
else:
    print('Sorry, that is not a palindrome.')
