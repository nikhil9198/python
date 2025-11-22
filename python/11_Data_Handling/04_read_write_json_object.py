import json
# Define a JSON data
data={
    "name":"John",
    "age":26,
    "city":"NewYork"
}

# print(type(data))
# Convert python object into json string
jsonString=json.dumps(data,indent=4)
# print(type(jsonString))
# print("JSON String",jsonString)

# Convert JSON string back into Python string
pythonObject=json.loads(jsonString)
print(type(pythonObject))
print("Python Object",pythonObject)