# CS 141 Lab 10
# line.py
#
# Modified by: Michelle Chen
#
# Defines a class that represents a line segment on a Cartesian plane.

from carpoint import Point

class LineSegment:

    # The class constructor that initializes a line segment by storing
    # the two end points in the two attributes self.pointA and self.pointB.
    def __init__(self, pointA, pointB):
        self.pointA = pointA
        self.pointB = pointB
    
    # Returns Point A endpoint
    def endPointA(self):
        return self.pointA
    
    # Returns Point B endpoint
    def endPointB(self):
        return self.pointB
    
    # Determines if the line segment is vertical or parallel to the x-axis
    # True if vertical, false otherwise
    def isVertical(self):
        return self.pointA.xCoord - self.pointB.xCoord == 0
    
    # Determines if the line segment is horizontal or parallel to the x-axis
    # True if vertical, false otherwise
    def isHorizontal(self):
        return self.pointA.yCoord - self.pointB.yCoord == 0
    
    # Determines if two line segments are parallel
    # True if parallel, false otherwise
    def isParallel(self, otheLine):
        if (self.pointA.xCoord - self.pointB.xCoord) != 0 and \
           (otheLine.pointA.xCoord - otheLine.pointB.xCoord) != 0:
            # Ensures that no error message is printed
            return ((self.pointA.yCoord - self.pointB.yCoord) / (self.pointA.xCoord - self.pointB.xCoord)) \
                   == ((otheLine.pointA.yCoord - otheLine.pointB.yCoord) / (otheLine.pointA.xCoord - otheLine.pointB.xCoord))
        
        elif (self.pointA.xCoord - self.pointB.xCoord) == 0 and \
             (otheLine.pointA.xCoord - otheLine.pointB.xCoord) == 0:
            # Two vertical lines are going to be parallel
            return True
        
        else:
            return False
    
    # Determines the length of the line segment
    def length(self):
        return self.pointA.distance(self.pointB)
    
    # Determines the slope of the line segment
    # Returns false if the line segment is vertical
    def slope(self):
        if (self.pointA.xCoord - self.pointB.xCoord) != 0:
            return (self.pointA.yCoord - self.pointB.yCoord) / (self.pointA.xCoord - self.pointB.xCoord)
        
        else:
            return False
    
    # Determines the midpoint of a line segment
    def midPoint(self):
        return Point((self.pointA.xCoord + self.pointB.xCoord) / 2, (self.pointA.yCoord + self.pointB.yCoord) / 2)


