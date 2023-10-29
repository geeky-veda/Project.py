mylist=[22,4,16,59,69]

print("This is my list: ",mylist)
print("1. Append an element")
print("2. Insert an element")
print("3. Append a list to the given list")
print("4. Modify an existing element")
print("5. Delete an existing element from its position")
print("6. Delete an existing element with a given value")
print("7. Sort the list in the ascending order")
print("8. Sort the list in descending order")
print("9. Display the list.")

while True:
    ch=int(input("Enter the option above (1-9) you want to perform: "))

    if ch==1:
        element = eval(input("Enter the element to be appended: "))
        mylist.append(element)
        print("The element has been appended\n",mylist)
    elif ch==2:
        element = eval(input("Enter the element to be inserted: "))
        pos = int(input("Enter the position:"))
        mylist.insert(pos, element)
        print("The element has been inserted\n",mylist)
    elif ch==3:
        newlist = eval(input("Enter the list to be appended: "))
        mylist.extend(newlist)
        print("The list has been appended\n",mylist)
    elif ch==4:
        i = int(input("Enter the position of the element to be modified: "))
        x=len(mylist)
        if i < x:
            newElement = eval(input("Enter the new element: "))
            oldElement = mylist[i]
            mylist[i] = newElement
            print("The element", oldElement, "has been modified\n",mylist)
        else:
            print("Position of the element is more then the length of list")
    elif ch==5:
        i = int(input("Enter the position of the element to be deleted: "))
        if i < len(mylist):
            element = mylist.pop(i)
            print("The element", element, "has been deleted\n",mylist)
        else:
            print("Position of the element is more then the length of list")
    elif ch==6:
        element = int(input("\nEnter the element to be deleted: "))
        if element in mylist:
            mylist.remove(element)
            print("\nThe element", element, "has been deleted\n",mylist)
        else:
            print("\nElement", element, "is not present in the list")
    elif ch==7:
        mylist.sort()
        print("\nThe list has been sorted :",mylist)
    elif ch==8:
        mylist.sort(reverse=True)
        print("\nThe list has been sorted in reverse order")
    elif ch==9:
        print("\nThe list is:", mylist)

    next_op = input("Let's do next operation? (yes/no): ")
    if next_op == "no":
        break
    elif next_op == "yes":
        continue
    else:
        print("Choice is not valid")

