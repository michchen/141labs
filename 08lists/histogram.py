# CS 141 Lab 8
# histogram.py
#
# Created by: Michelle Chen
#
# Prompts the user for a file containing grades. Then creates a histogram
# of the grades.

file = input("Please enter the name of the file: ") + ".txt"
# Makes the name of the file that will be opened
grades = open(file, "r")

grade_count = [0] * 11
# Creates a list that keeps track of the frequency of scores

for score in grades:
    score = int(score)
    grade_count[score // 10] += 1
    # Adds to the frequency of scores to the list

print("Grade Distribution")
print("-" * 18)

for number in range (10,-1, -1):
    stars = "*" * grade_count[number]
    # produces the right number of stars depending on the frequency
    if number == 10:
        print("100     :" + stars)
    if number == 9:
        print("90 - 99 :" + stars)
    if number == 8:
        print("80 - 89 :" + stars)
    if number == 7:
        print("70 - 79 :" + stars)
    if number == 6:
        print("60 - 69 :" + stars)
    if number == 5:
        print("50 - 59 :" + stars)
    if number == 4:
        print("40 - 49 :" + stars)
    if number == 3:
        print("30 - 39 :" + stars)
    if number == 2:
        print("20 - 29 :" + stars)
    if number == 1:
        print("10 - 19 :" + stars)
    if number == 0:
        print("00 - 09 :" + stars)

grades.close()
# Closes the file