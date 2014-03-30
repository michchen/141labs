# CS 141 Lab 5
# tobinary.py
#
# Created by: Michelle Chen
# 
# Converts a positive integer into a binary string.

integer = int(input("Please input a positive integer: "))
binary = ""
binary_string = ""
# Creates new variables for later use

while integer < 0:
    integer = int(input("Must be a positive integer: "))
    # ensures that no negative numbers will be used

if integer == 0:
    print("0")
    # makes sure to print 0 if 0 is the input

while integer > 0:
    if integer % 2 == 0:
        binary = str("0")
        binary_string = binary + binary_string
        print(binary_string)
        # prints 0 if the remainder is 0 (if the number is even) and adds it to
        # a binary string
    else:
        binary = str("1")
        binary_string = binary + binary_string
        print(binary_string)
        # prints 1 and adds it onto the binary_string that has been building
    integer = integer // 2
