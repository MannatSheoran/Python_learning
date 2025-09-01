# Problem Statement:
# Write a program that prompts the user to enter a score between 0.0 and 1.0.
# - If the score is out of range, display "Bad score".
# - Otherwise, assign a grade:
#     >= 0.9 : A
#     >= 0.8 : B
#     >= 0.7 : C
#     >= 0.6 : D
#     < 0.6  : Fail
# - Use a function computegrade(score) to return the grade.
# - Handle invalid input using try/except.




def computegrade(score):
    
    if score>1.0 or score<0:
        return("Bad score")
    elif score>=0.9:
        return("A")
    elif score>=0.8:
        return("B")
    elif score>=0.7:
        return("C")
    elif score>=0.6:
        return("D")
    else:
        return("fail")

try:
    score=float(input("Enter the score from 0.0 to 1.0"))
except:
    print("Enter a valid float input")
    quit()
print(computegrade(score))
