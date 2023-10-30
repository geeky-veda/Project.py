l1=[10,20,10,200,20,30]
n=int(input("What do u want to find repeating: "))
count=0
for i in l1:
    if i==n:
        count+=1

print(n,"is repeated",count,"times")