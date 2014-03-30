# CS 141 Lab 4
# hailstone.py
#
# Modified by: Michelle Chen
# 
# This program generates the Hailstone sequence
# It starts with a positive number and continues to either
# divide it in half if the number is even
# or multiply it by 3 and adding 1 if it is odd.
# It then prints the results

number = int(input(" Please input a number: "))
print(number, end = " ")
# prints the initial value before entering the loop

while number > 1:
# ensures that only positive integers greater than 1 enter the loop
    if number % 2 == 0:
        number = number // 2
        print(number, end = " ")
        # even part of the Hailstone sequence
    else:
        number = (number * 3) + 1
        print(number, end = " ")
        # odd part
