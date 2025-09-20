l=[]
while True:
    num=input("Enter the number: ")
    if num=="done":
        break
    else:
        n=int(num)
        
        l.append(n)

print(l)
print("The maximum number of the numbers entered is ",max(l))
print("The minimum number of the numbers entered is ",min(l))