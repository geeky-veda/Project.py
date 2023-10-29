Amount = int(input("Enter the Amount: "))
Year = int(input("Enter the No.of.Year to Pay Amount: "))
Rate = float(input("Enter the Interest Rate: "))
simpleinterest = (Amount*Year*Rate)/100
total_amount = simpleinterest+Amount

print("Simple Interest = ",simpleinterest)
print("Total Amount Paid = ",total_amount)