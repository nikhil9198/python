list1=[]

while True:
    oprInput=int(input('''
    1. Push Element
    2. Pop Element
    3. Peak Element
    4. Display Stack
    5. Exit
    '''))
    if oprInput==1:
        userInput=input("Enter a value: ")
        list1.append(userInput)
        print(list1)
    elif oprInput==2:
        if len(list1)==0:
            print("Empty Stack")
        else:
            popElement=list1.pop()
            print("Pop element: ",popElement)
            print(list1)
    elif oprInput==3:
        if len(list1) == 0:
            print("Empty Stack")
        else:
            print("Last element of stack is: ",list1[-1])
    elif oprInput==4:
        print("Display Stack: ",list1)
    elif oprInput==5:
        break;
    else:
        print("Invalid Operation")
