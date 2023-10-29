num = int(input("Enter the sum of 'n' numbers: "))
if num<0:
    print("Enter Positive Number.")
else:
    sum=1
    while num>0:
        sum=sum*num
        num=num-1
    print(sum)