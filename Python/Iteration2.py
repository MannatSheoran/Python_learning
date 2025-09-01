''' Exercise 2: Write another program that prompts for a list of numbers as above
 and at the end prints out both the maximum and minimum of the numbers instead
 of the average.'''
num_list=[]
while True:
    word=input("Enter the number: ")
    if word == "done":
        break
    try:
        num=float(word)
    except:
        print("Enter valid input")
    
    else:
        num_list.append(num)
print(max(num_list))
print(min(num_list))

    
