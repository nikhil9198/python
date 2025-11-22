# Write and Read JSON data from a file
import json
# Define a JSON data
data={
    "name":"John",
    "age":26,
    "city":"NewYork"
}

# Write JSON data to a file
with open("json-data.json","w")as file:
    json.dump(data,file,indent=4)
print("JSON data has been written to json-data.json file")

# Read data from a file
# myData=open("json-data.json","r")
# print(json.load(myData))  # or
# loadData=json.load(myData)
# print(loadData)

# another method to read at the same time to write
with open("json-data.json","r")as file:
    loadData=json.load(file)
print(loadData)
