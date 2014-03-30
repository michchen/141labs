# CS 141 lab 2
# cylinder.py
#
# Modified by: Michelle Chen
#
# This program calculates the volume, surface area and circumference of
# a cylinder with values for the radius and height provided by the user

import math

floatRad = input("Enter the radius of the cylinder: ")
rad = float(floatRad)

floatHeight = input("Enter the height of the cylinder: ")
hei = float(floatHeight)

cir = 2*math.pi*rad
area = 2*math.pi*rad*hei
vol = math.pi*(rad**2)*hei

print("The circumference is", cir)
print("The surface area is", area)
print("the volume is", vol)