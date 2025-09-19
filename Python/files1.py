# Program to read a file line by line and print the total lines in the file.
# If the user enters the filename "na na boo boo", display a funny message instead.
# Handle normal files as usual and show error if the file does not exist.

import os
base_dir=os.path.dirname(__file__)

fint=input("Enter the filename:")
file_path=os.path.join(base_dir,fint)


if fint=="na na boo boo":
    print(" NA NA BOO BOO TO YOU- You have been punkd!")
    exit()

try:
    with open(file_path,"r") as f:
        count=0

        for line in f:      
            count=count+1


except:
    print("File does not exist")
    exit()


    

print("There were {} subject lines in {}".format(count,fint))



