# Create and save a data into byte object
import pickle
data={
    "name":"John",
    "age":27,
    "profession":"Software Engineer",
    "salary":"$3000",
    "Experience":"10+Years"
}
myData=pickle.dumps(data)
print(pickle.loads(myData))
