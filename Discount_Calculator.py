Amount = float(input("Enter the Amount of Product: "))
discount = float(input("Enter Discount Percentage: "))
discamount = Amount - Amount*discount/100

print("Before Discount =",Amount)
print("Discount = ",discount)
print("After Discount = ",discamount)
