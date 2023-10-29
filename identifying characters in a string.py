s="Gigabyte123555"
v=0
u=0
l=0
for i in s:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        v+=1
    elif(i=='A' or i=='B'or i=='C' or i=='D' or i=='E' or i=='F' or i=='G' or i=='H' or i=='J' or i=='K' or i=='L' or i=='M' or i=='N' or i=='O' or i=='P' or i=='Q' or i=='R' or i=='S' or  i=='T' or i=='U' or i=='V' or i=='W' or i=='X' or i=='Y' or i=='Z'):
        u+=1
    elif(i=='1' or i=='2' or i=='3' or i=='4' or i=='5' or i=='6' or i=='7' or i=='8' or i=='9' or i=='0'):
        l+=1
print(v)
print(u)
print(l)
