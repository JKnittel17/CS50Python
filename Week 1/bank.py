"""
Prompt:
In a file called bank.py, implement a program that prompts the user for a greeting. If the greeting starts with “hello”, output $0. If the greeting starts with an “h” 
(but not “hello”), output $20. Otherwise, output $100. Ignore any leading whitespace in the users greeting, and treat the users greeting case-insensitively.

"""

# Ask User for greeting  ----  strip + lower to make comparison easier
greeting = input("Greeting: ").strip().lower()

# Output $0 if greeting starts with "hello", $20 if greeting starts with "h" but not hello, otherwise output $100
if greeting.startswith("hello"):
    print("$0")
elif greeting.startswith("h"):
    print("$20")
else:
    print("$100")



"""
Alternative Solution: 

We could replace our 2nd elif statement with a statement that checks the first digit of "greeting" for "h"

greeting = input("Greeting: ").strip().lower()

if greeting.startswith("hello"):
    print("$0")
elif greeting[0] == "h":
    print("$20")
else:
    print("$100")

"""