str = "X-DSPAM-Confidence: 0.8475"
post=str.find(" ")
res=(str[post:])
res=float(res)
print(res)

