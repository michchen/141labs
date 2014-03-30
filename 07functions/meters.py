# CS141 - Lab 7
# meters.py
#
# Modified by: Michelle Chen
#
# Extracts a measurement given in feet and inches from the user, 
# then converts the measurement to meters and displays the result.  


# The main driver function.
def main():
    print("Enter a measurement.")
    feet = float(input("Enter the feet: "))
    inches = float(input("Enter the inches: "))
    conversion = convertToMeters( feet, inches )
    
    print(feet, "feet and", inches, "is", conversion, "meters")
  
# Converts the given measurement (feet and inches) to meters. The
# meters measurement is returned as a floating-point value.
def convertToMeters( feet, inches ):
    result = (feet * 12 + inches) / 39.37
    
    return result

# Call the main routine.  
main()  
