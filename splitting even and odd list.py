l1=[]
n=int(input("Enter the number of element to be added: "))
for i in range(0,n):
    e=int(input("Enter the element: "))
    l1.append(e)
print("What you want to separate\n","1.Even\n","2.Odd")
ch=int(input("Enter Your Choice(1/2):"))
while True:
    if ch==1:
        for x in l1:
            if(x%2!=0):
                l1.remove(x)
        print(l1)
    elif ch==2:
        for x in l1:
            if(x%2==0):
                l1.remove(x)
        print(l1)
    else:
        print("Invalid Input")
    break