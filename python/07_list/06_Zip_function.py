list1=[10,50,30,100,20,40]
list2=[2,40,70,34,80,30]
list3=[3,50,30,60,80]
length=len(list1)
for a,b,c in zip(list1,list2,list3):
    print(a,b,c)

# for i in range(length):
#     print(list1[i],list2[i])