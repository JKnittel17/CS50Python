"""
Prompt:
In a file called adieu.py, implement a program that prompts the user for names, one per line, until the user inputs control-d. Assume that the user will input at least one name. 
Then bid adieu to those names, separating two names with one and, three names with two commas and one and, and names with commas and one and, as in the below:
"""

names = []

# If only one name, print this variation
if len(names) == 1:

    print(f"Adieu, adieu, to {names[0]}")

# If two names, print this variation
elif len(names) == 2:

    print(f"Adieu, adieu, to {names[0]} and {names[1]}")

# If two names, print this variation
else:

    print("Adieu, adieu, to ", end="")

    # Iterate through names list - last line of list needs to be a bit different than the rest
    count = 0
    for name in names:

        if count != (len(names) - 1):

            print(f"{name}, ", end="")

            count += 1

        else:
            
            print(f"and {name}")


"""
Alternative Solution 1) I did not look at the hints originally, but the hints provide a module you can impot that makes this process much easier

import inflect
p = inflect.engine()

names = []

while True:

    # Get user name input and store into list
    try:

        names.append(input("Name: "))

    except EOFError:

        break

print("Adieu, adieu, to " + p.join(names))

"""