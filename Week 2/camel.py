"""
In a file called camel.py, implement a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case. 
Assume that the users input will indeed be in camel case.

"""

# Get input from user
camelCase = input("camelCase: ").strip()

# Print snake_case but do not go to new line
print("snake_case: ", end="")

# Iterate through variable camelCase, and print letter if lowercase, if uppercase print _ + lowercase letter
for i in camelCase:

    if i.isupper():
        print("_", i.lower(), sep="", end="")

    else:
        print(i, end="")