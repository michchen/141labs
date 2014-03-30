# CS 141 lab 12
# findstring.py
#
# Modified by:
#
# This program takes a word and a file from the user
# and displays the location of the first occurence of a word in a line.

import sys
import string

def main():
    if len(sys.argv) < 3:
        # Makes sure that there are enough arguments
        print("Missing arguments.")
        print("Usage: findstring.py <word> <filename>")
        sys.exit()
    # Assigns value
    word = sys.argv[1]
    filename = sys.argv[2]
    try:
        # Tries to open the file
        fileHandle = open(filename, "r")
    except IOError:
        # Throws error if file does not exist
        print("Could not open", filename)
        sys.exit()
    
    findAll(word, fileHandle)
    
##########You do not need to modify anything in this function ############

def findAll(search, fh):
    count = 0
    found = False
    for line in fh:
        pos = -1
        count += 1
        words = line.split()
        if words.count(search) > 0:
            pos = words.index(search) 
        if pos != -1:
            found = True
            print("Found",search,"as word",pos+1,"in line",count)
    if not found:
        print("The file does not contain the word",search)
    	
##########################################################################

main()

