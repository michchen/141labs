# CS141 lab 6
# mathtable.py
#
# Modified by: Michelle Chen
#
# A program that produces a table containing the squares,
# square roots, and log values for a sequence of numbers.

import math

table = open("table.txt", 'w')

BEGIN = 1.0   # starting value for x
END = 10.0    # ending value for x
INC = 0.5     # amount to increment x by
      
# Print the table header.      
print( "Mathematical Table\n", file = table )
print( "     x  |          x^2      sqrt(x)       log(x)", file = table )
print( "-" * 50 , file = table)
                          
# Print the table of values. 
x = BEGIN
while x <= END :
    xSqr = x * x
    xSqrt = math.sqrt(x)
    xLog = math.log(x)
  
    print( "%7.2f | %12.2f %12.2f %12.2f" % (x, xSqr, xSqrt, xLog), file = table)
    x += INC

print( "-" * 55 , file = table)

table.close()