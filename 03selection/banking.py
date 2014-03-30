# CS 141 Lab 3
# banking.py
#
# Modified by: Michelle Chen
#
# This program mimics a ATM menu system
# It allows clients to withdraw or deposit money
# It does not allow overdraws or deal with negative money. It outputs the
# remaining balance at the end

bal = 2010

print ("Welcome to the CS141 Bank")
transac = input("Please choose either  (D)eposit   (W)ithdrawal: ")
transac = transac.upper()
#capitalizes the response so that lower and upper case can be used.

if transac == "D" or transac == "W":
    amount = float(input("Please enter an amount: "))
    if amount < 0.0:
        print ("Amount must be >= 0.0")
        #verifies that the amount is positive
    elif transac == "W":
        if amount > bal:
            print ("You can not overdraw your account!!")
            #ensures that no overdraws can occur
        else:
            total = bal - amount
            print ("Your final balance is: ", total)
    else:
        total = bal + amount
        print ("Your final balance is: ", total)
        # if the deposit option is chosen it skips down here to find the balance
else:
    print("Invalid option.")
    # if w or d is not the input, it will end the program
        
                
    
