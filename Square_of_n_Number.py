num = int(input("Enter the sum of 'n' numbers: "))
if num<0:
    print("Enter Positive Number.")
else:
    sum=0
    while num>0:
        sum=sum+num**2
        num=num-1
print(sum)
