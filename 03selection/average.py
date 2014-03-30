# CS 141 Lab 3
# average.py 
#
# Modified by: Michelle Chen
#
# This program asks the user to enter three grades
# the program then reads these grades and calculate the average
# After the program computers the average it outputs a letter grade. 


grade1 = float(input(" Please input the 1st grade: "))
grade2 = float(input(" Please input the 2nd grade: "))
grade3 = float(input(" Please input the 3rd grade: "))
    
average= (grade1 + grade2 + grade3) / 3
print(" Average score = ", average)
#round function is to round the input to the nearest integer.
#Victoria informed us it was okay to remove the round feature.
    
if average >= 60.0:
    print(" The student passed.")
    if average >= 90.0:
        print(" And got a A.")
    elif average >= 80.0:
        print(" And got a B.")
    elif average >= 70.0:
        print(" And got a C.")
    else:
        print(" And got a D.")
else:
    print (" The student failed.")
    print (" And got a F.")