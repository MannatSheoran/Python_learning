# Program to read a file line by line and print the total lines in the file.
# If the user enters the filename "na na boo boo", display a funny message instead.
# Handle normal files as usual and show error if the file does not exist.



fint=input("Enter the filename:")
if fint=="na na boo boo":
    print(" NA NA BOO BOO TO YOU- You have been punkd!")
    exit()

try:
    fname=open(fint)
except:
    print("File does not exist")
    exit()

count=0

for line in fname:      
    count=count+1
    

print("There were {} subject lines in {}".format(count,fint))



