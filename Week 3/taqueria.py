"""
Prompt:
In a file called taqueria.py, implement a program that enables a user to place an order, prompting them for items, one per line, until the user inputs control-d 
(which is a common way of ending ones input to a program). After each inputted item, display the total cost of all items inputted thus far, prefixed with a dollar sign 
($) and formatted to two decimal places. Treat the users input case insensitively. Ignore any input that isnt an item. Assume that every item on the menu will be titlecased.
"""
# Define menu dictionary
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main ():

    # Define cost counter
    cost = 0.00
    
    while True:

        try: 
            
            # Get item
            item = input("Item: ").title()
            
            # See if item is in menu
            if item in menu:
                
                # Update cost + output accumulated cost with 2 decimals
                cost += menu[item]
                print(f"Total: ${cost:.2f}")
        
        # Check for control-d
        except EOFError:

            print()
            break

main()