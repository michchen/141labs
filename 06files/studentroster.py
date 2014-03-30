# CS 141 Lab 6
# studentroster.py
#
# Modified by: Michelle Chen
# 
# This program extracts data from students.txt
# and creates a student roster of the students' names, classifications, and GPA
# It also lists the average GPA

student_data = open("students.txt", "r")
roster = open("roster.txt", "w")
# Opens the data files

line = student_data.readline()
# Reads the data from the file student_data

count = 0
sum_gpa = 0
iteration = 0
name = ""
grade = ""
gpa = 0

print("Name              Class       GPA  ", file = roster)
print("-" * 35, file = roster)
# Prints the header

while line != "":
    line = line.strip()
    # Strips the new line
    iteration += 1
    # Counts the iterations to make sure that the right line of data is used
    if iteration % 4 == 2:
        name = line
    if iteration % 4 == 0:
        if line == "1":
            grade = "Freshman"
        elif line == "2":
            grade = "Sophomore"
        elif line == "3":
            grade = "Junior"
        elif line == "4":
            grade = "Senior"
        else:
            grade = "Other"
        print("%-17s %-11s %1.2f" % (name, grade, gpa), file = roster)
        # Prints all of the data in one line with proper spacing
    if iteration % 4 == 3:
        gpa = float(line)
        sum_gpa += gpa
        count += 1
        # Adds up the gpas and counts the number of gpas that were input
    line = student_data.readline()
    # Reassigns line to the student_data file

average = sum_gpa / count

print("-" * 35, file = roster)
print("Average GPA: %20.2f" % (average), file = roster)

student_data.close()
roster.close()