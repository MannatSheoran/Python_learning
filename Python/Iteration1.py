'''Exercise 1: Write a program which repeatedly reads integers until the user enters
 “done”. Once “done” is entered, print out the total, count, and average of the
 integers. If the user enters anything other than a integers, detect their mistake
 using try and except and print an error message and skip to the next integers.'''


word=0
total=0
count=0
avg=0
while True:
    word=input("Enter the integer")
    if word=="done":
        break;

    try:
        user_input=int(word)
    except:
        print("Invalid input")
        continue
    total=total+user_input
    count=count+1
    avg=total/count

print(total,count,avg)





    
