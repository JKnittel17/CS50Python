"""
Prompt:
In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer, and then outputs, as a percentage 
rounded to the nearest integer, how much fuel is in the tank. If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty. And if 99% or 
more remains, output F instead to indicate that the tank is essentially full.

If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. (It is not necessary for Y to be 4.) Be sure to catch any exceptions like 
ValueError or ZeroDivisionError.
"""

def main ():

    # Prompt user for input
    result = get_fraction_and_convert()

    # Print Value
    print(f"{result}")


def get_fraction_and_convert():

    while True:

        try: 
            # Prompt user for input
            x, y = input("Fraction: ").split("/")

            # Convert x/y to int
            x = int(x)
            y = int(y)
            
            # Ensure x <= y and that x is not negative
            # Return needed result dependening on use case
            if x <= y and x >= 0:

                if (x / y) * 100 <= 1:
                    return "E"
                
                elif (x / y) * 100 >= 99:
                    return "F"
                
                else:
                    return str(int((x / y) * 100)) + "%"
            
        # If error - keep prompting
        except (ValueError, ZeroDivisionError):
            pass


main()