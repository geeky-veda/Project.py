p = float(input("Enter principal amount: "))
R = float(input("Enter annual interest rate: "))
n = int(input("Enter number of months: " ))

r = R/(12*100)

emi = p * r * ((1+r)**n)/((1+r)**n - 1)

print("Monthly EMI = ", emi)