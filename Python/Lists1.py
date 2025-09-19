''' List all unique words, sorted in alphabetical order, that are stored in a file romeo.txt containing a subset of Shakespeare’s
 work. To get started, download a copy of the file www.py4e.com/code3/romeo.txt. Create a list of unique words, which will contain the final result. Write a program to
 open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split function. For each word, check to see if the word is
 already in the list of unique words. If the word is not in the list of unique words, add it to the list. When the program completes, sort and print the list of unique
whwords in alphabetical order.'''

import os

base_dir = os.path.dirname(__file__)

fname = input("Enter the file name: ")

file_path = os.path.join(base_dir, fname)



try:
    with open(file_path, "r") as f:
        fint = f.read()

except:
    print("file does not exist")
    exit()


word=fint.split()
unique=[]

for j in word:
    if j not in unique:
        unique.append(j)

unique.sort()
print(unique)