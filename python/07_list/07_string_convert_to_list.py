# userInput=input("Enter the string:")
# print(userInput)
# list1=userInput.split()
# print(list1)

list1=[]
for i in range(1,5):
    userInput=input("Enter a string- "+str(i)+": ")
    list1.append(userInput)
    print(userInput)
print(list1)