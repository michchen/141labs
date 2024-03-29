# CS141 lab 4
# mathtable.py
#
# Modified by: Michelle Chen
#
# A program that produces a table containing the squares,
# square roots, and log values for a sequence of numbers.

import math

BEGIN = 0.5   # starting value for x
END = 9.5    # ending value for x
INC = 0.5     # amount to increment x by
      
# Print the table header.      
print( "Mathematical Table\n" )
print( "     x  |          x^2      sqrt(x)       log(x)" )
print( "-" * 50)
                          
# Print the table of values. 
x = BEGIN
while x <= END :
    x += INC
    xSqr = x * x
    xSqrt = math.sqrt(x)
    xLog = math.log(x)
    
    print( "%7.2f | %12.2f %12.2f %12.2f" % (x, xSqr, xSqrt, xLog) )

print( "-" * 50 )

