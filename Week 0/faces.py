"""
Prompt:
Before there were emoji, there were emoticons, whereby text like :) was a happy face and text like :( was a sad face. 
Nowadays, programs tend to convert emoticons to emoji automatically!

In a file called faces.py, implement a function called convert that accepts a str as input and returns that same input with any :) 
converted to 🙂 (otherwise known as a slightly smiling face) and any :( converted to 🙁 (otherwise known as a slightly frowning face). All other text should be returned unchanged.

Then, in that same file, implement a function called main that prompts the user for input, calls convert on that input, and prints the result. 
Youre welcome, but not required, to prompt the user explicitly, as by passing a str of your own as an argument to input. Be sure to call main at the bottom of your file.
"""

# Define Main function
def main():

    # Gather User Input
    text = input()
    # Call convert function and store converted text into a variable
    converted_text = convert(text)
    # Print result
    print(converted_text)

# Define convert function
def convert(text):
    
    # Convert ":)" to happy emoji, and ":(" to sad emoji face
    text1 = text.replace(":)","🙂")
    text2 = text1.replace(":(","🙁")

    # Return converted text
    return text2

# Run the program
main()