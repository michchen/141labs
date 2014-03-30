# CS 141 Lab 11
#
# Created by: Michelle Chen
#
# This program keeps track of the number of vertices in a polygon and returns
# information regarding the polygon's vertices. It also allows you to input
# more vertices

from carpoint import Point

class Polygon:
    # initializes the instance variables
    def __init__(self, vertex1, vertex2, vertex3):
        self.vertList = [vertex1, vertex2, vertex3]
    
    # returns the length of the list
    def numVertices(self):
        return len(self.vertList)
    
    # returns a vertex value given the positive index number
    # otherwise it returns false
    def getVertex(self, ndx):
        if ndx >= 0:
            try:
                return self.vertList[ndx]
            except IndexError:
                return False
        
        return False
    
    # Finds the vertex
    def findVertex(self, vertex):
        count = 0
        if count <= len(self.vertList):
            for item in self.vertList:
                count += 1
                # checks whether the vertex is in the list or not
                if vertex.isEqual(item):
                    return self.vertList.index(item)
        
        return False
    
    # inserts the vertex into the list
    def insertVertex(self, vertex, afterNdx):
        count = 0
        dump = []
        if count <= len(self.vertList):
            for item in self.vertList:
                count += 1
                # checks whether or not item is in list
                if vertex.isEqual(item):
                    dump.append(item)
        
        # if the item isn't already in the list and the index value is positive
        # it keeps going
        if dump == [] and afterNdx >= 0:
            if afterNdx < len(self.vertList):
                self.vertList.insert((afterNdx + 1), vertex)
                # adds value to list after the index value
                return True
            elif afterNdx == len(self.vertList):
                self.vertList.insert(0, vertex)
                # inserts it at 0 if afterNdx is equal to the length of the list
                return True
            else:
                return False
        
        return False

    
    def deleteVertex(self, ndx):
        if ndx < len(self.vertList) and len(self.vertList) > 3 and ndx >= 0:
            # deletes vertex values
            self.vertList.pop(ndx)
            return True
        
        return False
    
    def perimeter(self):
        count = 0
        perimeter = 0     
        for count in range(0, (len(self.vertList) - 1)):
            # uses the distance formula from carpoint to configure the perimeter
            perimeter += (self.vertList[count]).distance(self.vertList[(count + 1)])                
            count += 1
        
        # adds up the distance from the first vertex to the last
        perimeter += self.vertList[len(self.vertList) - 1].distance(self.vertList[0])
        
        return float(perimeter)
    