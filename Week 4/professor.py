"""
Prompt:
In a file called professor.py, implement a program that:
Prompts the user for a level, n. If the user does not input 1, 2, or 3, the program should prompt again.
Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with digits. No need to support operations other than addition (+).
Prompts the user to solve each of those problems. If an answer is not correct (or not even a number), the program should output EEE and prompt the user again, allowing the user 
up to three tries in total for that problem. If the user has still not answered correctly after three tries, the program should output the correct answer.
The program should ultimately output the users score: the number of correct answers out of 10.
Structure your program as follows, wherein get_level prompts (and, if need be, re-prompts) the user for a level and returns 1, 2, or 3, and generate_integer returns a randomly 
generated non-negative integer with level digits or raises a ValueError if level is not 1, 2, or 3:
"""

import random


def main():
    
    level = get_level()

    round, score = 1, 0

    while round <= 10:

        # Made 3rd function game_round to keep main code a little cleaner 
        if game_round(level) == True:

            score += 1
        
        round += 1

    print(f"Score: {score} / 10")


# Prompt user for level
def get_level():
    
    while True: 

        try: 

            level = int(input("Level: "))

            if level in [1,2,3]:

                return level

        except ValueError:

            pass

# Generate random int dependant on level
def generate_integer(level):

    match level:
           
        case 1:
               
            x = random.randint(0,9)
            y = random.randint(0,9)
        
        case 2: 

            x = random.randint(10,99)
            y = random.randint(10,99)

        case 3:

            x = random.randint(100,999)
            y = random.randint(100,999)
           
    return x, y

# Iterate through 1 round of the game
def game_round(level):

     guess = 0

     x, y = generate_integer(level)

     while guess < 3:

        try:

            answer = int(input(f"{x} + {y} = "))

            if answer != (x + y):

                print("EEE")

                guess += 1

                if guess == 3:

                    print(f"{x} + {y} = {x + y}")
                    return False

            else:

                return True

        except ValueError:

                guess += 1
                print("EEE")

                if guess == 3:

                    print(f"{x} + {y} = {x + y}")
                    return False
                 

if __name__ == "__main__":

    main()