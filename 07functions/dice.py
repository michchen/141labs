# CS 141 Lab 7
# dice.py
#
# Modified by: Michelle Chen
#
# Generates two randomly generated die faces when the user hits enter.

import random

# The main driver routine. 

def main():
    print("Simulate the rolling of a die.\n")
    action = input("Press <ENTER> to roll the dice or enter <q> to quit: ")
    while action != 'q' :
        value = rollDie()
        value_two = rollDie()
        print("You rolled a", value, "and a", value_two)
        print( buildDie(value) )
        print( buildDie(value_two) )
    
        action = input("Press <ENTER> to roll the die or enter <q> to quit: ")
    
  
# Simulates the rolling of a 6-sided die using the random number 
# generator. The face value is returned.

def rollDie() :
    die_roll = random.randint(1,6)
    
    return die_roll
    
  
# Builds and returns a text-based version of the die face as a string 
# based on the face value passed as a argument.

def buildDie( faceValue ) :
    if faceValue == 1:
        face = "  ----- \n |     | \n |  *  | \n |     | \n  ----- "
    if faceValue == 2:
        face = "  ----- \n |*    | \n |     | \n |    *| \n  ----- "
    if faceValue == 3:
        face = "  ----- \n |*    | \n |  *  | \n |    *| \n  ----- "
    if faceValue == 4:
        face = "  ----- \n |*   *| \n |     | \n |*   *| \n  ----- "
    if faceValue == 5:
        face = "  ----- \n |*   *| \n |  *  | \n |*   *| \n  ----- "
    if faceValue == 6:
        face = "  ----- \n |*   *| \n |*   *| \n |*   *| \n  ----- "
        
    return face
  
    
# Call the main routine.  
main()  
  
