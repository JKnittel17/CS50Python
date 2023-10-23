""""
Prompt:
In deep.py, implement a program that prompts the user for the answer to the Great Question of Life, 
the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.

"""


# Prompt user for their answer
# I chose to strip and convert to lowercase for easier comparision on Output portion of code
text = input("What is the answer to the Great Question of Life, the Universe and Everything? ").lower().strip()

# Evaluate user input, and output Yes or No
match text:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")


""""
Alternative solution using if statement with "or":

text = input("What is the answer to the Great Question of Life, the Universe and Everything? ").lower().strip()

if text == "42" or text == "forty-two" or text == "forty two":
    print("Yes")
else:
    print("No")
    
    
"""