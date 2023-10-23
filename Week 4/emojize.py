"""
Prompt:
In a file called emojize.py, implement a program that prompts the user for a str in English and then outputs the “emojized” version of that str, converting any codes 
(or aliases) therein to their corresponding emoji.
"""

import emoji

# Prompt User
response = input("Input: ")

# Print emojized response
print(emoji.emojize(f"Ouput: {response}", language="alias"))


"""
Alternate Solution 1)

import emoji

# Prompt User
response = input("Input: ")

# Convert Emoji
output = emoji.emojize(response, language="alias")

# Print emojized response
print("Output:", output)

"""