# CS 141 Lab 9
# concordance.py
#
# Created by: Michelle Chen
# 
# Keeps track of where and how many times a word appears in a file.

import string
# import string to get rid of punctuation later

file = open("concordance.txt", "r")
dictionary = {}
line_count = 0
word_list = []

for line in file:
    line_count += 1
    line = line.split()
    # strips the new line and initializes a count to keep track of lines
    for word in line:
        word = word.lower()
        word = word.strip(string.punctuation)
        # lower case everything and strip the punctuation
        if word not in dictionary:
            dictionary[word] = []
            word_list.append(word)
            # creates a new entry if the word is not already in the dictionary
            # Creates a word list to use later in the print statement
        dictionary[word].append(line_count)
        # appends the line number count to the dictionary

print("Word          Line Number")
print("-" * 25)

word_list.sort()
# Sorts the list alphabetically
for word in word_list:
    print("%-13s %s" % (word, dictionary[word]))

file.close()