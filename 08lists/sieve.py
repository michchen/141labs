# CS 141 Lab 8
# sieve.py
#
# Created by: Michelle Chen
# 
# Computes a list of prime numbers going from 2 to some user specified number N.

primes_list = []
candidate_list = []
# Creates two empty lists for the integers

upper_limit = int(input("Please enter the upper limit: "))

count = 1

while count < upper_limit:
    count += 1
    candidate_list.append(count)
    # Creates a list of numbers in candidate_list

while candidate_list != []:
    prime = candidate_list.pop(0)
    primes_list.append(prime)
    stop_number = len(candidate_list) - 1
    # Figures out the right place to start the for loop
    for x in range (stop_number, -1, -1):
        if candidate_list[x] % prime == 0:
            candidate_list.pop(x)
        # Gets rid of multiples

for number in primes_list:
    print(number)
    # Prints out all primes onto their own line
