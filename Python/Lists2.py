import os
dir=os.path.dirname(__file__)
fint=input("Enter the file name: ")
file_path=os.path.join(dir,fint)

try:
    with open(file_path,"r") as f:
        count=0
        for i in f:
            if i.startswith("From "):
                print(i.split()[1])
                count=count+1

except:
    print("The file does not exist")
    exit()

print(f"There are {count} lines in the file with From as the first word")

