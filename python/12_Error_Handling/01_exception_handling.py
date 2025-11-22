# Exapmle 1
# num1=10
# num2=1
#
# try:
#     result=num1/num2
# except ZeroDivisionError :
#     print("Don't divide it by zero, Try Again")
# else:
#     print(result)
# finally:
#     print("Execution Completed")

# Example 2
num1=int(input("Enter first Number : "))
num2=int(input("Enter second number : "))

try:
    result=num1/num2
except (TypeError,ZeroDivisionError)as e:
    print(f"An error occurred {e} ")
else:
    print(result)
finally:
    print("Execution Completed")