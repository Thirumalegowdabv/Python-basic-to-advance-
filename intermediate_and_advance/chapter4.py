# Introduction to JSON

# JSON = JavaScript Object Notation.

# It is a lightweight format for storing and exchanging data.

# Syntax is similar to Python dictionaries but with some differences:

# JSON keys and string values use double quotes " ".

# Data types supported: string, number, boolean, null, array, object.

# Example JSON data:

{
  "name": "Alice",
  "age": 25,
#   "is_student": false,
  "skills": ["Python", "Data Science"],
  "address": {
    "city": "Bengaluru",
    "pincode": 560001
  }
}

# Basic JSON operations in Python

# Python has a built-in module: json


#  Converting JSON ↔ Python
import json

# JSON string
json_data = '{"name": "Alice", "age": 25, "is_student": false}'

# Convert JSON string to Python dictionary
python_dict = json.loads(json_data)
print(python_dict)   # {'name': 'Alice', 'age': 25, 'is_student': False}
print(type(python_dict))  # <class 'dict'>

# Convert Python dict back to JSON string
json_string = json.dumps(python_dict)
print(json_string)   # {"name": "Alice", "age": 25, "is_student": false}
print(type(json_string))  # <class 'str'>


# Note:

# json.loads() → JSON string → Python object

# json.dumps() → Python object → JSON string



#  Reading and Writing JSON Files
# Writing Python data to a JSON file
import json

data = {
    "name": "Bob",
    "age": 30,
    "skills": ["Java", "React"]
}

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)  # indent for pretty printing

# Reading JSON file
with open("data.json", "r") as file:
    content = json.load(file)
    print(content)



# Working with Complex / Nested JSON

# Nested data structures are common in APIs.

import json

json_data = '''
{
  "company": "TechCorp",
  "employees": [
    {"name": "Alice", "role": "Developer"},
    {"name": "Bob", "role": "Manager"}
  ]
}
'''

data = json.loads(json_data)

# Access nested data
print(data["company"])  # TechCorp
print(data["employees"][0]["name"])  # Alice

# Loop through employees
for emp in data["employees"]:
    print(emp["name"], "-", emp["role"])
    
    

# Advanced JSON: Custom Encoding/Decoding
# Custom Encoder (e.g., handling Python objects)
import json
from datetime import datetime

class Employee:
    def __init__(self, name, join_date):
        self.name = name
        self.join_date = join_date

# Custom encoder function
def employee_encoder(obj):
    if isinstance(obj, Employee):
        return {"name": obj.name, "join_date": obj.join_date.isoformat()}
    raise TypeError("Object not serializable")

emp = Employee("Alice", datetime.now())

json_data = json.dumps(emp, default=employee_encoder, indent=4)
print(json_data)



# Custom Decoder
def employee_decoder(dct):
    if "join_date" in dct:
        dct["join_date"] = datetime.fromisoformat(dct["join_date"])
    return dct

decoded = json.loads(json_data, object_hook=employee_decoder)
print(decoded)



# Practical Tips & Use Cases

#  Working with APIs: JSON is the most common data format returned by APIs.

#  Use json.load() for files and json.loads() for strings.

#  Use indent=4 in json.dump() for pretty printing.

#  For faster parsing of huge JSON files, consider ujson or orjson libraries.



# Quick Recap

# json.dumps() ↔ Python → JSON string

# json.loads() ↔ JSON string → Python

# json.dump() ↔ Python → JSON file

# json.load() ↔ JSON file → Python

# Custom encoder/decoder → handle complex objects