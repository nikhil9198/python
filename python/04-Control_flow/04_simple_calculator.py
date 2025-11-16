val1=eval(input("Enter a First value: " ))
val2=eval(input("Enter a Second value: " ))
oper=input("Enter an Operator: " )
if oper=="+":
    print(val1+val2)
elif oper=="-":
    print(val1-val2)
elif oper=="*":
    print(val1*val2)
elif oper=="/":
    print(val1/val2)
else:
    print("Invalid Operator")
