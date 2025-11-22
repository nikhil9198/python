# Write and Read Data from Files

# Write data into a file
import pickle
data={
    "name":"John",
    "age":27,
    "profession":"Software Engineer",
    "salary":"$3000",
    "Experience":"10+Years"
}
writeData=open("my-data.txt", "wb")
pickle.dump(data,writeData)
writeData.close()

# Read data into a file
myFile=open("my-data.txt","rb")
loadData=pickle.load(myFile)
print(loadData)