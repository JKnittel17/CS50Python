"""
Prompt:
In a file called grocery.py, implement a program that prompts the user for items, one per line, until the user inputs control-d (which is a common way of ending ones 
input to a program). Then output the users grocery list in all uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted 
that item. No need to pluralize the items. Treat the users input case-insensitively.
"""


def main():

    # Create 2 lists --- 1 will track total items, 1 will track unique items
    list = []
    unique_items = []

    while True:

        try:

            # Prompt User for item
            item = input("Add an item to the list: ").strip().upper()


            # Add item to list
            list.append(item)

            # if current input not in unique items, add it to unique items list
            if item not in unique_items:

                unique_items.append(item)

        except EOFError:

            # Alphabetize unique_items list
            unique_items.sort()

            # Print out grocery list and count for each unique item
            for n in unique_items:

                print(list.count(n), n)


            break

main()


"""

Alternate Solution 1) We could use a dictionary instead of 2 lists -- which is probably more optimal

groceries = {}

while True:

    try:

        item = input().strip().upper()

        if item in groceries:
            groceries[item] += 1

        else:
            groceries[item] = 1

    except EOFError:

        for item in sorted(groceries):
            print(groceries[item], item)

        break

"""