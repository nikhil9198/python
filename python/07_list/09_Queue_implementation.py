list1=[]

while True:
    oprInput=int(input('''
    1. Push Element
    2. Pop First Element
    3. Front Element
    4. Rear Element
    5. Display Queue
    6. Exit
    '''))
    if oprInput==1:
        userInput=input("Enter a value: ")
        list1.append(userInput)
        print(list1)
    elif oprInput==2:
        if len(list1)==0:
            print("Empty Queue")
        else:
            del list1[0]
            print(list1)
    elif oprInput==3:
        if len(list1) == 0:
            print("Empty Queue")
        else:
            print("First element of Queue is: ",list1[0])
    elif oprInput==4:
        if len(list1) == 0:
            print("Empty Queue")
        else:
            print("Last Queue Element: ",list1[-1])
    elif oprInput==5:
        print("Display Queue: ", list1)
    elif oprInput==6:
        break
    else:
        print("Invalid Operation")
