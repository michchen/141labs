# CS 141 lab 2
# line.py
#
# Modified by: Michelle Chen
#
# This program calculates the length of a line segment
# defined by two Cartisian coordinates (x0,y0) and (x1, y1)

import math

# Set the values of the two points that define the line.
intStr = input("Enter the x-coordinate for the first point: ")
x0 = int(intStr)
intStrY0 = input("Enter the y-coordinate for the first point: ")
y0 = int(intStrY0)
intStrX1 = input("Enter the x-coordinate for the second point: ")
x1 = int(intStrX1)
intStrY1 = input("Enter the y-coordinate for the second point: ")
y1 = int(intStrY1)

# Calculate the length of the line over the x- and y-axes.
base = x1 - x0 
height = y1 - y0 

# Calculate the length of the line itself.
length = math.sqrt(base ** 2 + height ** 2)

# Display the result on the screen.
print("The length of the line is", length)

slope = (height/base)

print("The slope of the line is", slope)