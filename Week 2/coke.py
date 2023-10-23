"""
Prompt:
Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.

In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. Once the 
user has inputted at least 50 cents, output how many cents in change the user is owed. Assume that the user will only input integers, and ignore any integer that 
isnt an accepted denomination.
"""

def main():

    # Define total amount needed, 0.50
    remaining_needed = 50
    
    while remaining_needed > 0:
        
        # Tell the user reamining amount needed
        print(f"Amount Due: {remaining_needed}")

        # Get coin from user --- store as an int
        coin = int(input("Insert Coin: "))

        # If coin is valid, subtract coin value from remaining needed, and tell user remaining amount needed if > 0
        if coin in [5, 10, 25]:

            remaining_needed -= coin

    # Tell user change owed
    print(f"Change Owed: {abs(remaining_needed)}")


main()


"""
Alternative Solution 1)

When comparing the coin to the accepted values, we could instead do a less complex version in the if statement:

if coin == "5" or coin == "10" or coin == "25":

"""