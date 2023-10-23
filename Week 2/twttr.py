"""
Prompt:
When texting or tweeting, its not uncommon to shorten words to save time or space, as by omitting vowels, much like Twitter was originally called twttr. In a file called 
twttr.py, implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in 
uppercase or lowercase.

"""

def main():
    
    # Prompt user for input
    result = input("Input: ")

    # Ouput 
    print("Output: ",end="")

    # For each letter in result, compare lowercase value to list of vowels. If not in list, print the letter. 
    for letter in result:
        
        if letter.lower() not in ["a", "e", "i", "o", "u"]:
            print(letter, end="")


main()