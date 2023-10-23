"""
Prompt:
In a file called figlet.py, implement a program that:

Expects zero or two command-line arguments:
Zero if the user would like to output text in a random font.
Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font, and the second of the two should be the name of the font.

Prompts the user for a str of text.
Outputs that text in the desired font.

If the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a font, the program should exit via sys.exit with an error message.
"""

import sys, random
from pyfiglet import Figlet

figlet = Figlet()

while True:

    # Check # of command line arguments
    if len(sys.argv) not in [1,3]:
        
        sys.exit("Additional Command Line Arguments must be 0 or 2")

    # If there are two additional command line arguments, check to make sure 1st is "-f" and second is valid font type
    if len(sys.argv) == 3:
        
        if sys.argv[1] not in ["-f", "--font"]:

            sys.exit("First command line argument must be -f or --font")
        
        elif sys.argv[2] not in figlet.getFonts():

            sys.exit("Font chosen is not valid")

        else:

            figlet.setFont(font=sys.argv[2])


    # If no command line arguments given, choose random font
    else:

        figlet.setFont(font=random.choice(figlet.getFonts()))


    # Prompt User for Input and print using font chosen or random font, break out of program
    response = input("Input: ")
    print(figlet.renderText(response))
    break
