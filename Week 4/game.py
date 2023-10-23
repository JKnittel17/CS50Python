"""
Prompt:
In a file called game.py, implement a program that:

Prompts the user for a level, n. If the user does not input a positive integer, the program should prompt again.
Randomly generates an integer between 1 and n, inclusive, using the random module.
Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
If the guess is larger than that integer, the program should output Too large! and prompt the user again.
If the guess is the same as that integer, the program should output Just right! and exit.
"""

import sys, random

def main():

    level = get_level()
    eval_guess(level)


# Get upper limit from user, ensure it is positive integer
def get_level():

    while True: 

        try: 

            level = int(input("Level: "))

            if level > 0:

                return level

        except ValueError:

            pass

# Determine random number between 1 - level, prompt user for guess, provide feedback on guess to user
def eval_guess(level):

    answer = random.randrange(1, level)

    while True: 

        try:

            guess = int(input("Guess: "))

            if guess > 0 and guess > answer:

                print("Too Large!")

            elif guess > 0 and guess < answer:

                print("Too Small!")

            elif guess > 0 and guess == answer:

                print("Just Right!")
                break

        except ValueError:

            pass


main()