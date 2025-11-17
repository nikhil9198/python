# Syntax of list Comprehension
# [expression for item in list]

list1=[]
for i in range(1,51):
    list1.append(i)
print(list1)

list2=[ind for ind in range(1,51)if ind % 2 == 1]
print(list2)