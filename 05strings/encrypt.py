# CS 141 Lab 5
# encrypt.py
#
# Created by: Michelle Chen
#
# This program substitutes for each letter in a text with a string
# some fixed number of positions away. The punctuation remains unchanged.

import string

shift = int(input("Please enter a shift amount: "))
message = input("Please enter a message: ")
new_message = ""
# Creates a new string for the encrypted message to be printed

for char in message:
    if char in string.ascii_lowercase:
        char = ord(char) - ord('a')
        char = (char + shift) % 26
        char = chr(char + ord('a'))
        new_message += char
        # Adds the encryped characters to the new string
    else:
        new_message += char
        # Adds the punctuation as is to the string

print("The encrypted message is: ",new_message)
