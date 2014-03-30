# CS 141 lab 11
# fraction.py
#
# Modified by: Michelle Chen
#
# A class that represents a fraction or rational number.

import math
import sys

class Fraction:
    def __init__(self, num, den):
       # The denominator can not be zero. If it is, abort the program.
        if den == 0: 
            sys.exit("Divide by zero")
        
       # Compute the greatest common divisor and reduce the numerator
       # and the denominator.
        div = gcd(num, den)
        self.num = abs(num // div)
        self.den = abs(den // div)
      
       # A negative fraction will be indicated by a negative numerator. 
        if num * den < 0: 
            self.num = -self.num
    
    def __str__(self):
        return str(self.num) + "/" + str(self.den) 
    
    def getNum(self):
        return str(self.num)
    
    def getDen(self):
        return str(self.den)
        
    def __add__(self, rhsFrac):
        newFrac = Fraction((rhsFrac.den * self.num + self.den * rhsFrac.num),(self.den * rhsFrac.den))
        
        return Fraction.__str__(newFrac)
        
    def __sub__(self, rhsFrac):
        subFrac = Fraction((rhsFrac.den * self.num + self.den * -rhsFrac.num),(self.den * rhsFrac.den))
        
        return Fraction.__str__(subFrac)
        
    def __neg__(self):
        self.num = -self.num
        
        return Fraction.__str__(self)
        
    def __eq__(self, rhsFrac):
        return self.num == rhsFrac.num and self.den == rhsFrac.den
      

# greatest common divisor function
# param:
# bigger  int   one of the two numbers which is bigger than the other
# smaller int   one of the two numbers which is smaller than the other
#
# return: the greatest common divisor of bigger and smaller
def gcd(bigger, smaller):
    while smaller != 0:
        temp = smaller
        smaller = bigger % smaller
        bigger = temp
    return bigger


