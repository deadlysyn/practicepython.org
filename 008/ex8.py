#!/usr/bin/env python
#
# practicepython.org exercise 8:
# rock-paper-scissors

import getpass

choices = ['rock', 'paper', 'scissors']
message = """
Welcome to the exciting game of rock-paper-scissors!

Two players take turn chosing one of rock, paper, or
scissors and the infinitely wise computer decides who
wins the game! What could possibly go wrong?

Note: Your choice will not be printed to make it more
interesting for your opponent...
"""

print(message)

while True:
    print('Please type rock, paper or scissors or type quit to exit...')
    p1 = getpass.getpass(prompt='Player #1: ', stream=None).lower()
    p2 = getpass.getpass(prompt='Player #2: ', stream=None).lower()
    if p1 == 'quit' or p2 == 'quit':
        print('Bye.')
        break
    elif p1 not in choices or p2 not in choices:
        print('What was that?  Try again.')
    elif p1 == 'rock' and p2 == 'scissors':
        print('Player 1 scores!')
    elif p1 == 'scissors' and p2 == 'paper':
        print('Player 1 scores!')
    elif p1 == 'paper' and p2 == 'rock':
        print('Player 1 scores!')
    else:
        print('Player 2 scores!')
