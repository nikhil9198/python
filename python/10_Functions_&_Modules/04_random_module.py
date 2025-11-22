import random
list1=[1,20,5,30,45,90]
print("Randint : ",random.randint(1,20)) # both 1 and 10 include to printing random values
print("Randrange : ",random.randrange(1,20)) # 1 is included but 20 is not include to printing random values
print("Choice : ",random.choice(list1))
print("Random : ",random.random()) # it will return only 0 to 1 floating values exclude 1
random.shuffle(list1)
print("Shuffled list : ",list1)
print("Uniform : ",random.uniform(1,20))