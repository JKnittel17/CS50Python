"""
Prompt: In a file called indoor.py, implement a program in Python that prompts the user for input and then outputs that same input in lowercase. 
        Punctuation and whitespace should be outputted unchanged. You are welcome, but not required, to prompt the user explicitly, 
        as by passing a str of your own as an argument to input.
"""

# A user prompt is not needed per the question above
text = input().lower()
print(text)




"""
Alternate Solution:

We could technically do this in one line of code, but it is a little bit more confusing then breaking it out into 2 lines like the above. 
The benefit of the below solution would be that no variable is needed to store the user input - which may or may not be what is desired. 

print(input().lower())

"""