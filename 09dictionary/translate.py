# CS 141 Lab 9
# translate.py
#
# Created by: Michelle Chen
#
# Translates a user input shorthand text message into proper English.

translation = open("textabbv.txt", "r")

word = translation.readline()
iteration = 0
dictionary = {}
key = ""
value = ""
list_count = -1

while word != "":
    word = word.strip()
    iteration += 1
    if iteration % 2 == 1:
        key = word
        # Makes sure the right line becomes the keys
    if iteration % 2 == 0:
        value = word
    dictionary[key] = value
    word = translation.readline()
    # Moves onto the next line in the file

text = (input("Please enter a text message: ")).split()
for word in text:
    list_count += 1
    if word in dictionary.keys():
        text[list_count] = dictionary[word]
        # Replaces the word at the index number in the list with proper English
        
text = ' '.join(text)
# Joins the list together

print("The translated text is: ", text)
translation.close()