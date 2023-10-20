""""
Prompt: In a file called playback.py, implement a program in Python that prompts the user for 
        input and then outputs that same input, replacing each space with ... (i.e., three periods).
"""



# This is an easy solution. I have added ".strip" as well (even though it was not asked for) to eliminate any leading or trailing spaces.
# This solution first asks for an input from the user with no prompt, strips it, replaces remaining spaces with "..." and stores it in the variable text. We then print text.

text = input().strip().replace(" ","...")
print(text)





"""
Alternate Solutions:

*** Alternate Solution 1) Same as original solution but broken out more. 

text = input().strip().replace(" ","...")
new_text = text.strip().replace(" ","...")
print(new_text)


*** Alternate Solution 2) Way more complicated than it needs to be - but it works. Including it cause it may connect with how someone else would have done this. This is
what I came up with originally before realizing there was a much simpler way to do the same thing. 

text = input("Please enter a sentence: ").split()

for n in range(len(text)):
    if n == (len(text) - 1):
        print(text[n])
    else:
        print(text[n], end="...")

"""
