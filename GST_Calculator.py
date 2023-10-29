original_amount = int(input("Enter the amount: "))
rate = int(input("Enter the GST Rate: "))
gst_amount = (original_amount*rate)/100
net_amount = original_amount+gst_amount

print("GST Amount = ",gst_amount)
print("Net Amount = ",net_amount)