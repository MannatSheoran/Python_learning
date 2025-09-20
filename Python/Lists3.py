
while True:
    num=input("Enter the number: ")
    if num=="done":
        break
    else:
        n=int(num)
        l=[]
        l.append(n)


print("The maximum number of the numbers entered is ",max(l))
print("The maximum number of the numbers entered is ",min(l))