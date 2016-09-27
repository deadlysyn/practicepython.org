#!/usr/bin/env python
#
# practicepython.org exercise 9:
# number guessing game

import random


num = random.randint(1, 9)
guesses = 0

while True:
    guess = input('Guess the number 1-9 (type exit to quit): ')
    # technically this gets incremented even on typos...
    guesses += 1

    # Make sure we have a number...
    if guess.lower() == 'exit':
        break
    else:
        try:
            guess = int(guess)
        except ValueError:
            print('Was that a number? Try again.')
            continue

    # Test the number...
    if guess == num:
        print('You chose wisely!')
        print('Generating a new number...')
        num = random.randint(1, 9)
    elif guess > num:
        print('Too high!')
    elif guess < num:
        print('Too low!')
    else:
        print('Try again!')

print('You made {0} guesses.'.format(guesses))