''' Write a program to prompt for a file name, and then read through
 the file and look for lines of the form:
 X-DSPAM-Confidence: 0.8475
 When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart
 the line to extract the floating-point number on the line. Count these lines and
 then compute the total of the spam confidence values from these lines. When you
 reach the end of the file, print out the average spam confidence.
'''

fint=input("Enter the filename:")

try:
    fname=open(fint)
except:
    print("File does not exist")
    exit()


count = 0
total = 0.0

for line in fname:
    if line.startswith("X-DSPAM-Confidence:"):
        
        pos = line.find(":")
        value = float(line[pos+1:].strip())
        total += value
        count += 1


avg = total / count
print("Average spam confidence:", avg)





