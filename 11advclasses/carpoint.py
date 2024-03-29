# CS 141 Lab 10
# carpoint.py
# 
# Modified by: Michelle Chen
#
# Defines a class that represents a Cartesian point.


class Point:

     # The class constructor that initializes an instance of the class.
    def __init__(self, x, y):
        self.xCoord = x
        self.yCoord = y
        
     # Returns a string representation of the point. Automatically used
     # by the print() function when printing a Point object.
    def __str__(self):
        return '(' + str(self.xCoord) + ',' + str(self.yCoord) + ')'
    
     # Returns the x-coordinate of the point  
    def getX(self):
        return self.xCoord
        
     # Returns the y-coordinate of the point
    def getY(self):
        return self.yCoord
     
     # Returns true if the point is (0,0) and false otherwise
    def isOrigin(self):
        return self.xCoord == 0 and self.yCoord == 0
        
     # Returns true if this point is the same as the otherPoint, and
     # false otherwise.
    def isEqual(self, otherPoint):
        return self.xCoord == otherPoint.xCoord and \
                self.yCoord == otherPoint.yCoord
        
     # Returns the distance between this point and the otherPoint.
    def distance(self, otherPoint):
        import math
        return math.sqrt((self.xCoord - otherPoint.xCoord) ** 2 + (self.yCoord - otherPoint.yCoord) ** 2)

        
