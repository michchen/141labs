# CS 141 Lab 4
# average2.py 
#
# Modified by: Michelle Chen
#
# This program asks the user to enter grades until they enter -1.
# the program then reads these grades and calculates the average
# After the program computes the average it outputs a letter grade. 

count = 0
grade = float(input(" Please input a grade: "))
grade_sum = 0

while grade != -1:
    grade_sum += grade
    count += 1
    grade = float(input(" Please input a grade: "))

if count != 0: 
# if the first value entered is -1, nothing prints
    average = (grade_sum) / count
    print(" Average score = ", round(average))
    #round function is to round the input to the nearest integer.

    if average >= 60.0:
        if average >= 90.0:
            print(" Average grade: A")
            print(" Great job! You did exceptional work.")
        elif average >= 80.0:
            print(" Average grade: B")
            print(" You did above average work.")
        elif average >= 70.0:
            print(" Average grade: C")
            print(" You did average work.")
        else:
            print(" Average grade: D")
            print(" You marginally passed.")
    else:
        print (" Average grade: F")
        print (" Not good! You failed.")