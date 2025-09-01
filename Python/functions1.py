# Problem Statement:
# Write a program to calculate an employee's gross pay.
# - Prompt the user for hours worked and hourly rate.
# - If hours > 40, pay overtime at 1.5 times the hourly rate.
# - Implement a function computepay(hours, rate) to handle the calculation.



def pay_computation(hours,rate):
    
    

    if hours>40:
        overtime_hour=hours-40.0
        enhanced_rate=1.5*rate
        pay=40*rate
        overtime=overtime_hour*enhanced_rate
        return overtime + pay
    
    else:
        pay=hours*rate
        return pay

try:
        hours=float(input("Enter the number of hours"))
        rate=float(input("enter the rate per hour"))
except:
        print("Error, please enter a float input")
        quit()
print(pay_computation(hours,rate))

