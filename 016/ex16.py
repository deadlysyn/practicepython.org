#!/usr/bin/env python
#
# practicepython.org exercise 16:
# password generator

import random


# charsets used to construct passwords
LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
NUMS = '0123456789'
SPECIALS = '`~!@#$%^&*()-_+=[]{}|\:;"\'<>,.?,/'
# potentially troublesome characters to exclude if gen_pass is
# called with ambiguous=False
AMBIGUOUS = '0O1lI|$*\'"`'
# TODO: convert to file?
WORDLIST = ['module', 'whether', 'conditionally', 'executing', 'common']


def get_num(*, prompt='Number? '):
    """prompt for a number"""
    num = 0
    while True:
        try:
            num = int(input(prompt))
        except ValueError:
            print('Was that a number? Try again!')
            continue
        else:
            break
    return num


# random.sample can raise ValueError if sample (password
# length) is longer than population.
def gen_pass(*, pw_length=10, use_nums=True, use_special=True,
             no_dupes=False, no_ambiguous=True):
    """generate pseudo-random password of desired length"""
    # Build up desired population of characters
    charset = LETTERS
    if use_nums:
        charset += NUMS
    if use_special:
        charset += SPECIALS
    if no_ambiguous:
        charset = ''.join([x for x in charset if x not in AMBIGUOUS])

    if no_dupes:
        x, tmp = pw_length, []
        while x > 0:
            val = ''.join(random.sample(charset, 1))
            if val not in tmp:
                tmp.append(val)
                x -= 1
        return ''.join(tmp)
    else:
        return ''.join(random.sample(charset, pw_length))


# The exercise calls this the "simple" password, but given
# the right list of words a "passphrase" could both be
# easier to remember and have more entropy than shorter
# "random" passwords!
def gen_simple_pass(*, num_words=3):
    """generate simple password from wordlist"""
    return ' '.join(random.sample(WORDLIST, num_words))


if __name__ == '__main__':
    choice = input('Would you like a (S)imple or (R)andom password? (sR) ')
    length = get_num(prompt='How long of a password? ')
    if choice.lower() == 's':
        print('Chosing ' + str(length) + ' words for simple password...')
        print(gen_simple_pass(num_words=length))
    else:
        print('Generating ' + str(length) + ' random characters...')
        print(gen_pass(pw_length=length,
                       no_dupes=True,
                       no_ambiguous=False))
